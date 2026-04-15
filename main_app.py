import React, { useState } from 'react';
import { 
  LayoutDashboard, 
  Home, 
  BarChart3, 
  LogOut, 
  Bell, 
  Search, 
  TrendingUp, 
  Zap, 
  CheckCircle2, 
  AlertTriangle,
  Menu,
  PlusCircle,
  FileText,
  Download,
  Box,
  FileCode,
  BookOpen
} from 'lucide-react';

const App = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [currentPage, setCurrentPage] = useState('Home');
  const [isSidebarOpen, setSidebarOpen] = useState(true);

  // ข้อมูลจำลองสำหรับสายการผลิต
  const productionLines = [
    { id: 'L01', status: 'Running', efficiency: '98%', output: 1250, energy: '12kW' },
    { id: 'L02', status: 'Running', efficiency: '95%', output: 1100, energy: '14kW' },
    { id: 'L03', status: 'Warning', efficiency: '82%', output: 850, energy: '10kW' },
    { id: 'L04', status: 'Running', efficiency: '97%', output: 1300, energy: '15kW' },
    { id: 'L05', status: 'Stopped', efficiency: '0%', output: 0, energy: '1kW' },
  ];

  if (!isLoggedIn) {
    return <LoginPage onLogin={() => setIsLoggedIn(true)} />;
  }

  return (
    <div className="flex h-screen bg-gray-50 text-slate-800 font-sans">
      {/* Sidebar */}
      <aside className={`${isSidebarOpen ? 'w-72' : 'w-20'} bg-[#0f172a] text-white transition-all duration-300 flex flex-col shrink-0`}>
        <div className="p-8 flex items-center gap-3">
          <div className="w-10 h-10 bg-emerald-500 rounded-xl flex items-center justify-center font-black text-white italic shadow-lg shadow-emerald-500/20">S</div>
          {isSidebarOpen && <span className="font-black text-2xl tracking-tighter">SNAPCON</span>}
        </div>

        <nav className="flex-1 mt-2 px-4 space-y-1">
          <NavItem 
            icon={<Home size={22} />} 
            label="Home" 
            active={currentPage === 'Home'} 
            expanded={isSidebarOpen}
            onClick={() => setCurrentPage('Home')}
          />
          <NavItem 
            icon={<LayoutDashboard size={22} />} 
            label="My Dashboard" 
            active={currentPage === 'My Dashboard'} 
            expanded={isSidebarOpen}
            onClick={() => setCurrentPage('My Dashboard')}
          />
          
          {isSidebarOpen && (
            <div className="mt-10 px-2">
              <p className="text-[11px] font-black text-slate-500 uppercase tracking-[0.2em] mb-4 pl-2">System Resources</p>
              <div className="space-y-3">
                <ResourceItem icon={<FileCode size={18} />} label="DWG file" />
                <ResourceItem icon={<FileText size={18} />} label="Data sheet" />
                <ResourceItem icon={<BookOpen size={18} />} label="Catalog" />
              </div>
            </div>
          )}
        </nav>

        <div className="p-6 border-t border-slate-800/50">
          {isSidebarOpen && (
            <div className="mb-6 p-4 bg-slate-800/40 rounded-2xl border border-slate-700/50">
              <p className="text-[10px] text-slate-500 font-black uppercase tracking-wider mb-1">Authenticated Engineer</p>
              <p className="text-sm font-bold text-emerald-400">Watanabe San</p>
            </div>
          )}
          <button 
            onClick={() => setIsLoggedIn(false)}
            className="flex items-center gap-4 px-4 py-3 w-full text-slate-400 hover:text-white hover:bg-white/5 rounded-xl transition-all"
          >
            <LogOut size={20} />
            {isSidebarOpen && <span className="text-sm font-bold">Sign Out</span>}
          </button>
        </div>
      </aside>

      {/* Main Content Area */}
      <main className="flex-1 flex flex-col overflow-hidden">
        {/* Header */}
        <header className="h-20 bg-white border-b border-gray-100 flex items-center justify-between px-8 shrink-0 shadow-sm z-10">
          <div className="flex items-center gap-4">
            <button onClick={() => setSidebarOpen(!isSidebarOpen)} className="p-2.5 hover:bg-gray-100 rounded-xl transition-colors text-slate-400">
              <Menu size={22} />
            </button>
            <div className="h-6 w-[1px] bg-gray-200 mx-2 hidden md:block"></div>
            <div className="flex items-center gap-2 text-sm font-bold text-slate-400">
              <span>Management</span>
              <span className="text-slate-300">/</span>
              <span className="text-emerald-600 font-black">{currentPage}</span>
            </div>
          </div>

          <div className="flex items-center gap-6">
            <div className="relative hidden lg:block">
              <Search className="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400" size={18} />
              <input 
                type="text" 
                placeholder="Search resources..." 
                className="pl-12 pr-6 py-2.5 bg-gray-100 border-transparent rounded-2xl text-sm focus:ring-2 ring-emerald-500/20 focus:bg-white focus:border-emerald-100 outline-none w-72 transition-all font-medium"
              />
            </div>
            <button className="relative p-2 text-slate-400 hover:text-emerald-600 hover:bg-emerald-50 rounded-xl transition-all">
              <Bell size={22} />
              <span className="absolute top-1.5 right-1.5 w-4 h-4 bg-red-500 text-white text-[9px] font-black flex items-center justify-center rounded-full border-2 border-white shadow-sm">3</span>
            </button>
            <div className="h-10 w-[1px] bg-gray-100"></div>
            <div className="flex items-center gap-3">
              <div className="text-right hidden sm:block">
                <p className="text-xs font-black text-slate-800">Watanabe San</p>
                <p className="text-[10px] text-slate-400 font-bold uppercase tracking-tighter">Senior Lead</p>
              </div>
              <div className="w-11 h-11 bg-emerald-500 rounded-2xl flex items-center justify-center text-white font-black text-lg shadow-lg shadow-emerald-500/20">
                W
              </div>
            </div>
          </div>
        </header>

        {/* Dynamic Content */}
        <div className="flex-1 overflow-y-auto bg-[#f8fafc] p-10">
          {currentPage === 'Home' ? (
            <HomePage lines={productionLines} />
          ) : (
            <MyDashboardPage />
          )}
        </div>
      </main>
    </div>
  );
};

// Nav Link Component
const NavItem = ({ icon, label, active, expanded, onClick }) => (
  <button 
    onClick={onClick}
    className={`
      flex items-center gap-4 px-4 py-3.5 w-full rounded-2xl transition-all mb-1
      ${active 
        ? 'bg-emerald-600 text-white shadow-xl shadow-emerald-900/40' 
        : 'text-slate-500 hover:bg-white/5 hover:text-slate-200'}
    `}
  >
    <span className={active ? 'text-white' : 'text-slate-500'}>{icon}</span>
    {expanded && <span className="font-bold text-sm tracking-tight">{label}</span>}
  </button>
);

// New Resource Item UI (Updated as per image)
const ResourceItem = ({ icon, label }) => (
  <button className="w-full flex items-center gap-4 p-4 bg-slate-800/40 hover:bg-slate-800 transition-all rounded-2xl border border-slate-700/50 group text-left">
    <div className="bg-emerald-500/10 p-2.5 rounded-xl group-hover:bg-emerald-500 group-hover:text-white text-emerald-500 transition-all shadow-inner">
      {icon}
    </div>
    <div className="flex-1">
      <span className="text-sm font-bold text-slate-200 block">{label}</span>
      <span className="text-[10px] text-slate-500 font-bold uppercase tracking-widest group-hover:text-emerald-400 transition-colors">Download File</span>
    </div>
    <Download size={16} className="text-slate-600 group-hover:text-white transition-colors" />
  </button>
);

const LoginPage = ({ onLogin }) => (
  <div className="h-screen w-screen bg-[#020617] flex items-center justify-center p-6 relative overflow-hidden">
    {/* Ambient Glows */}
    <div className="absolute -top-24 -right-24 w-96 h-96 bg-emerald-500/20 blur-[100px] rounded-full"></div>
    <div className="absolute -bottom-24 -left-24 w-96 h-96 bg-blue-600/10 blur-[100px] rounded-full"></div>
    
    <div className="w-full max-w-md bg-white rounded-[2.5rem] shadow-2xl overflow-hidden relative z-10 border border-white/10">
      <div className="bg-emerald-600 p-12 text-center text-white relative">
        <div className="w-20 h-20 bg-white/20 rounded-3xl mx-auto flex items-center justify-center font-black text-4xl mb-6 italic shadow-inner backdrop-blur-md">S</div>
        <h1 className="text-3xl font-black tracking-tighter">SNAPCON</h1>
        <p className="text-emerald-100 text-[10px] font-black uppercase tracking-[0.3em] mt-3 opacity-70">Industrial Management v1.5</p>
      </div>
      <div className="p-12">
        <div className="space-y-6">
          <div className="space-y-2">
            <label className="text-[10px] font-black text-slate-400 uppercase tracking-widest pl-1">Employee ID</label>
            <input type="text" placeholder="SC-ENG-000" className="w-full px-6 py-4 bg-gray-50 border border-gray-100 rounded-2xl focus:ring-4 ring-emerald-500/10 focus:bg-white outline-none transition-all font-bold text-slate-700 placeholder:text-slate-300" />
          </div>
          <div className="space-y-2">
            <label className="text-[10px] font-black text-slate-400 uppercase tracking-widest pl-1">Access Token</label>
            <input type="password" placeholder="••••••••" className="w-full px-6 py-4 bg-gray-50 border border-gray-100 rounded-2xl focus:ring-4 ring-emerald-500/10 focus:bg-white outline-none transition-all font-bold text-slate-700 placeholder:text-slate-300" />
          </div>
          <button 
            onClick={onLogin}
            className="w-full py-5 bg-emerald-600 hover:bg-emerald-700 text-white font-black rounded-2xl transition-all shadow-xl shadow-emerald-600/30 active:scale-[0.98] uppercase tracking-[0.15em] text-xs mt-4"
          >
            Authorize Access
          </button>
        </div>
      </div>
    </div>
  </div>
);

const HomePage = ({ lines }) => (
  <div className="max-w-7xl mx-auto">
    <div className="flex flex-col md:flex-row justify-between items-start md:items-end mb-12 gap-6">
      <div>
        <h2 className="text-4xl font-black text-slate-900 tracking-tight">Plant Performance</h2>
        <p className="text-slate-500 text-sm font-medium mt-2 max-w-lg leading-relaxed">System-wide monitoring of efficiency, thermal loads, and output metrics for the current operational cycle.</p>
      </div>
      <div className="flex gap-4">
        <button className="px-6 py-3 bg-white border border-gray-200 rounded-2xl text-xs font-black text-slate-700 hover:bg-gray-50 flex items-center gap-2 shadow-sm transition-all">
          <FileText size={18} className="text-slate-400" /> Export OEE
        </button>
        <button className="px-6 py-3 bg-emerald-600 text-white rounded-2xl text-xs font-black hover:bg-emerald-700 flex items-center gap-2 shadow-xl shadow-emerald-600/30 transition-all active:scale-95 uppercase tracking-wider">
          <PlusCircle size={18} /> New Entry
        </button>
      </div>
    </div>

    {/* Quick Analysis Grid */}
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 mb-12">
      <StatCard label="Overall OEE" value="94.2%" change="+1.2%" icon={<Zap size={24} className="text-emerald-500" />} />
      <StatCard label="Daily Output" value="4,500" change="+420" icon={<TrendingUp size={24} className="text-emerald-500" />} />
      <StatCard label="Critical Alerts" value="03" change="-1" icon={<AlertTriangle size={24} className="text-amber-500" />} isWarning />
      <StatCard label="System Status" value="Stable" change="UPTIME" icon={<CheckCircle2 size={24} className="text-blue-500" />} />
    </div>

    {/* Production Lines Table */}
    <div className="bg-white rounded-[2rem] border border-gray-100 shadow-xl shadow-slate-200/50 overflow-hidden">
      <div className="px-10 py-7 border-b border-gray-50 flex justify-between items-center bg-gray-50/30">
        <h3 className="font-black text-slate-800 tracking-tight uppercase text-xs tracking-[0.1em]">Real-time Line Telemetry</h3>
        <div className="flex items-center gap-3 bg-emerald-50 px-4 py-1.5 rounded-full">
            <div className="w-2 h-2 bg-emerald-500 rounded-full animate-ping"></div>
            <span className="text-[10px] font-black text-emerald-700 uppercase tracking-widest">Live Feed</span>
        </div>
      </div>
      <div className="overflow-x-auto">
        <table className="w-full text-left">
          <thead className="text-slate-400 text-[10px] uppercase tracking-[0.2em] font-black border-b border-gray-50 bg-gray-50/20">
            <tr>
              <th className="px-10 py-6">Identity</th>
              <th className="px-10 py-6">Status</th>
              <th className="px-10 py-6">Efficiency</th>
              <th className="px-10 py-6">Gross Output</th>
              <th className="px-10 py-6">Energy</th>
              <th className="px-10 py-6 text-right">Action</th>
            </tr>
          </thead>
          <tbody className="text-sm divide-y divide-gray-50">
            {lines.map((line) => (
              <tr key={line.id} className="hover:bg-gray-50/50 transition-colors group">
                <td className="px-10 py-7 font-black text-slate-900">{line.id}</td>
                <td className="px-10 py-7">
                  <span className={`inline-flex items-center gap-2 px-4 py-1.5 rounded-xl text-[10px] font-black uppercase tracking-tight ${
                    line.status === 'Running' ? 'bg-emerald-50 text-emerald-700' : 
                    line.status === 'Warning' ? 'bg-amber-50 text-amber-700' : 'bg-red-50 text-red-700'
                  }`}>
                    <div className={`w-2 h-2 rounded-full ${
                        line.status === 'Running' ? 'bg-emerald-500' : 
                        line.status === 'Warning' ? 'bg-amber-500' : 'bg-red-500'
                    }`}></div>
                    {line.status}
                  </span>
                </td>
                <td className="px-10 py-7">
                  <div className="flex items-center gap-4">
                    <div className="w-28 h-2 bg-gray-100 rounded-full overflow-hidden">
                      <div className="h-full bg-emerald-500 transition-all duration-1000 shadow-sm" style={{ width: line.efficiency }}></div>
                    </div>
                    <span className="font-black text-slate-700 text-xs">{line.efficiency}</span>
                  </div>
                </td>
                <td className="px-10 py-7 text-slate-600 font-bold underline decoration-emerald-200 decoration-2 underline-offset-4">{line.output.toLocaleString()} <span className="text-[10px] text-slate-400 font-bold uppercase ml-1">U</span></td>
                <td className="px-10 py-7 text-slate-500 font-bold">{line.energy}</td>
                <td className="px-10 py-7 text-right">
                  <button className="p-2.5 bg-gray-50 text-slate-400 hover:text-emerald-600 hover:bg-emerald-50 rounded-xl transition-all">
                    <BarChart3 size={18} />
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  </div>
);

const MyDashboardPage = () => (
  <div className="max-w-7xl mx-auto">
    <div className="mb-12">
      <h2 className="text-4xl font-black text-slate-900 tracking-tight">Personal Workspace</h2>
      <div className="w-24 h-2 bg-emerald-500 mt-5 rounded-full shadow-lg shadow-emerald-500/20"></div>
    </div>

    <div className="grid grid-cols-1 lg:grid-cols-3 gap-10">
      <div className="lg:col-span-2 space-y-10">
        <div className="bg-white p-10 rounded-[2.5rem] border border-gray-100 shadow-xl shadow-slate-200/40">
          <h3 className="font-black text-slate-800 flex items-center gap-4 mb-8 uppercase text-xs tracking-[0.15em]">
            <div className="p-2 bg-emerald-50 rounded-lg"><CheckCircle2 size={20} className="text-emerald-600" /></div> Pending Workflow
          </h3>
          <div className="space-y-5">
            <TaskItem title="System Calibration - Line 03" priority="High" deadline="14:00 Today" />
            <TaskItem title="Weekly Maintenance Audit" priority="Medium" deadline="Tomorrow" />
            <TaskItem title="Inventory Cycle Count" priority="Low" deadline="Friday" />
          </div>
        </div>
      </div>

      <div className="space-y-10">
        <div className="bg-[#0f172a] text-white p-10 rounded-[2.5rem] shadow-2xl relative overflow-hidden group">
          <div className="absolute top-0 right-0 p-6 opacity-5 group-hover:rotate-12 transition-transform scale-150">
              <Box size={140} />
          </div>
          <div className="flex flex-col items-center text-center mb-10 relative z-10">
             <div className="w-20 h-20 rounded-3xl bg-emerald-500 flex items-center justify-center font-black text-3xl mb-4 shadow-xl shadow-emerald-500/20 italic">W</div>
             <p className="text-xl font-black tracking-tight">Watanabe San</p>
             <p className="text-[10px] text-emerald-400 uppercase tracking-[0.3em] font-black mt-2">Certified Admin</p>
          </div>
          <div className="space-y-5 pt-10 border-t border-slate-800 relative z-10">
            <ProfileStat label="Active Plants" value="05 Sites" />
            <ProfileStat label="Uptime Goal" value="99.9%" />
          </div>
        </div>
      </div>
    </div>
  </div>
);

const StatCard = ({ label, value, change, icon, isWarning }) => (
  <div className="bg-white p-8 rounded-[2rem] border border-gray-100 shadow-lg shadow-slate-200/30 flex items-start justify-between group hover:border-emerald-200 transition-all hover:-translate-y-1">
    <div>
      <p className="text-slate-400 text-[10px] font-black uppercase tracking-[0.15em] mb-3 group-hover:text-emerald-600 transition-colors">{label}</p>
      <h4 className="text-4xl font-black text-slate-900 tracking-tighter">{value}</h4>
      <p className={`text-[10px] font-black mt-3 inline-flex items-center gap-2 px-3 py-1 rounded-full ${isWarning ? 'bg-red-50 text-red-500' : 'bg-emerald-50 text-emerald-600'}`}>
        {change} <span className="text-slate-300 font-bold ml-1">Period</span>
      </p>
    </div>
    <div className="p-5 bg-gray-50 rounded-[1.5rem] group-hover:bg-emerald-50 group-hover:scale-110 transition-all duration-500 shadow-inner">
      {icon}
    </div>
  </div>
);

const TaskItem = ({ title, priority, deadline }) => (
  <div className="flex items-center justify-between p-6 bg-gray-50/50 hover:bg-white hover:shadow-xl hover:shadow-slate-200 transition-all rounded-[1.5rem] border border-transparent hover:border-gray-100 cursor-pointer group">
    <div className="flex items-center gap-5">
      <div className={`w-3 h-3 rounded-full shadow-sm ${
        priority === 'High' ? 'bg-red-500' : 
        priority === 'Medium' ? 'bg-amber-500' : 'bg-blue-500'
      }`}></div>
      <div>
        <p className="text-base font-black text-slate-800 group-hover:text-emerald-700 transition-colors">{title}</p>
        <p className="text-[10px] text-slate-400 font-bold uppercase tracking-widest mt-1">Closing: {deadline}</p>
      </div>
    </div>
    <span className={`text-[10px] font-black px-4 py-1.5 rounded-full tracking-widest uppercase ${
       priority === 'High' ? 'bg-red-50 text-red-600' : 'text-slate-400 bg-gray-200'
    }`}>
      {priority}
    </span>
  </div>
);

const ProfileStat = ({ label, value }) => (
  <div className="flex justify-between items-center text-[11px]">
    <span className="text-slate-500 font-black uppercase tracking-widest">{label}</span>
    <span className="font-black text-emerald-400 bg-emerald-400/10 px-3 py-1 rounded-lg">{value}</span>
  </div>
);

export default App;
