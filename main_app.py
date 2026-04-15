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
  BookOpen,
  ChevronRight
} from 'lucide-react';

const App = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [currentPage, setCurrentPage] = useState('Home');
  const [isSidebarOpen, setSidebarOpen] = useState(true);

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
      <aside className={`${isSidebarOpen ? 'w-80' : 'w-20'} bg-[#0a1e1a] text-white transition-all duration-500 flex flex-col shrink-0 shadow-2xl z-20`}>
        <div className="p-8 flex items-center gap-4">
          <div className="w-12 h-12 bg-emerald-500 rounded-2xl flex items-center justify-center font-black text-white italic shadow-[0_0_20px_rgba(16,185,129,0.4)]">S</div>
          {isSidebarOpen && (
            <div className="flex flex-col">
              <span className="font-black text-2xl tracking-tighter leading-none">SNAPCON</span>
              <span className="text-[10px] text-emerald-500 font-black tracking-[0.2em] mt-1">INDUSTRIAL AI</span>
            </div>
          )}
        </div>

        <nav className="flex-1 mt-4 px-4 space-y-1 overflow-y-auto no-scrollbar">
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
            <div className="mt-12 px-2 pb-8">
              <div className="flex items-center justify-between mb-6 px-2">
                <p className="text-[11px] font-black text-emerald-500/50 uppercase tracking-[0.25em]">Resources</p>
                <div className="h-[1px] flex-1 bg-emerald-500/10 ml-4"></div>
              </div>
              
              <div className="space-y-4">
                <ResourceItem 
                  icon={<FileCode size={20} />} 
                  label="DWG file" 
                  subLabel="Technical Drawing"
                />
                <ResourceItem 
                  icon={<FileText size={20} />} 
                  label="Data sheet" 
                  subLabel="Specifications PDF"
                />
                <ResourceItem 
                  icon={<BookOpen size={20} />} 
                  label="Catalog" 
                  subLabel="Product Guide 2024"
                />
              </div>
            </div>
          )}
        </nav>

        <div className="p-6 border-t border-white/5 bg-black/20">
          {isSidebarOpen && (
            <div className="mb-6 p-4 bg-emerald-500/5 rounded-2xl border border-emerald-500/10 flex items-center gap-3">
              <div className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></div>
              <div>
                <p className="text-[10px] text-slate-500 font-black uppercase tracking-wider">System Status</p>
                <p className="text-xs font-bold text-emerald-400">All Nodes Operational</p>
              </div>
            </div>
          )}
          <button 
            onClick={() => setIsLoggedIn(false)}
            className="flex items-center gap-4 px-4 py-3.5 w-full text-slate-400 hover:text-white hover:bg-white/5 rounded-2xl transition-all"
          >
            <LogOut size={20} />
            {isSidebarOpen && <span className="text-sm font-bold uppercase tracking-widest text-[11px]">Sign Out System</span>}
          </button>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 flex flex-col overflow-hidden bg-[#f1f5f9]">
        <header className="h-24 bg-white/80 backdrop-blur-md border-b border-slate-200 flex items-center justify-between px-10 shrink-0 z-10">
          <div className="flex items-center gap-6">
            <button onClick={() => setSidebarOpen(!isSidebarOpen)} className="p-3 hover:bg-slate-100 rounded-2xl transition-all text-slate-400 active:scale-90">
              <Menu size={24} />
            </button>
            <div className="hidden md:block">
              <h2 className="text-xl font-black text-slate-800 tracking-tight">{currentPage}</h2>
              <p className="text-[10px] text-slate-400 font-bold uppercase tracking-widest mt-0.5">Control Center / General View</p>
            </div>
          </div>

          <div className="flex items-center gap-6">
            <div className="relative hidden xl:block">
              <Search className="absolute left-5 top-1/2 -translate-y-1/2 text-slate-400" size={18} />
              <input 
                type="text" 
                placeholder="Search telemetry..." 
                className="pl-14 pr-6 py-3.5 bg-slate-100 border-transparent rounded-[1.25rem] text-sm font-bold focus:ring-4 ring-emerald-500/10 focus:bg-white focus:border-emerald-100 outline-none w-80 transition-all placeholder:text-slate-400"
              />
            </div>
            <div className="flex items-center gap-3">
              <button className="relative p-3 text-slate-400 hover:text-emerald-600 hover:bg-emerald-50 rounded-2xl transition-all">
                <Bell size={22} />
                <span className="absolute top-2.5 right-2.5 w-5 h-5 bg-emerald-600 text-white text-[10px] font-black flex items-center justify-center rounded-full border-4 border-white">2</span>
              </button>
              <div className="h-10 w-[1px] bg-slate-200 mx-2"></div>
              <div className="flex items-center gap-4 pl-2">
                <div className="text-right hidden sm:block">
                  <p className="text-xs font-black text-slate-900 leading-none">Watanabe San</p>
                  <p className="text-[9px] text-emerald-600 font-black uppercase tracking-widest mt-1.5 bg-emerald-50 px-2 py-0.5 rounded-md inline-block">Senior Lead</p>
                </div>
                <div className="w-12 h-12 bg-gradient-to-br from-emerald-400 to-emerald-600 rounded-[1.25rem] flex items-center justify-center text-white font-black text-xl shadow-lg shadow-emerald-500/20 border-2 border-white ring-1 ring-emerald-100">
                  W
                </div>
              </div>
            </div>
          </div>
        </header>

        <div className="flex-1 overflow-y-auto p-10 custom-scrollbar">
          {currentPage === 'Home' ? <HomePage lines={productionLines} /> : <MyDashboardPage />}
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
      flex items-center gap-4 px-5 py-4 w-full rounded-2xl transition-all duration-300 mb-2
      ${active 
        ? 'bg-gradient-to-r from-emerald-600 to-emerald-500 text-white shadow-[0_10px_20px_rgba(16,185,129,0.25)] scale-[1.02]' 
        : 'text-slate-400 hover:bg-white/5 hover:text-white'}
    `}
  >
    <span className={`${active ? 'text-white' : 'text-slate-500'} transition-colors`}>{icon}</span>
    {expanded && <span className="font-bold text-sm tracking-tight">{label}</span>}
    {active && expanded && <ChevronRight size={16} className="ml-auto opacity-50" />}
  </button>
);

// Updated Premium Resource Item (Matching the Uploaded Design)
const ResourceItem = ({ icon, label, subLabel }) => (
  <button className="w-full flex items-center gap-4 p-5 bg-white/5 hover:bg-white/10 transition-all duration-300 rounded-[1.5rem] border border-white/5 hover:border-emerald-500/30 group text-left relative overflow-hidden active:scale-[0.98]">
    {/* Subtle Glow Background */}
    <div className="absolute -right-4 -bottom-4 w-16 h-16 bg-emerald-500/5 blur-2xl group-hover:bg-emerald-500/10 transition-all"></div>
    
    <div className="w-12 h-12 flex items-center justify-center rounded-2xl bg-emerald-500/10 text-emerald-400 group-hover:bg-emerald-500 group-hover:text-white transition-all shadow-inner border border-emerald-500/20 group-hover:shadow-[0_0_15px_rgba(16,185,129,0.3)]">
      {icon}
    </div>
    
    <div className="flex-1 min-w-0">
      <span className="text-[13px] font-black text-white/90 block tracking-tight group-hover:text-emerald-400 transition-colors">{label}</span>
      <span className="text-[9px] text-slate-500 font-bold uppercase tracking-[0.1em] mt-0.5 block truncate group-hover:text-slate-400">{subLabel}</span>
    </div>

    <div className="w-8 h-8 flex items-center justify-center rounded-xl bg-white/5 text-slate-500 group-hover:bg-emerald-500/20 group-hover:text-white transition-all border border-white/5">
      <Download size={14} />
    </div>
  </button>
);

const LoginPage = ({ onLogin }) => (
  <div className="h-screen w-screen bg-[#020617] flex items-center justify-center p-6 relative overflow-hidden">
    <div className="absolute -top-24 -right-24 w-[500px] h-[500px] bg-emerald-500/10 blur-[120px] rounded-full"></div>
    <div className="absolute -bottom-24 -left-24 w-[500px] h-[500px] bg-blue-600/5 blur-[120px] rounded-full"></div>
    
    <div className="w-full max-w-md bg-white rounded-[3rem] shadow-[0_50px_100px_rgba(0,0,0,0.5)] overflow-hidden relative z-10 border border-white/10">
      <div className="bg-[#0a1e1a] py-16 text-center text-white relative">
        <div className="w-24 h-24 bg-emerald-500 rounded-[2rem] mx-auto flex items-center justify-center font-black text-5xl mb-6 italic shadow-[0_0_40px_rgba(16,185,129,0.4)]">S</div>
        <h1 className="text-4xl font-black tracking-tighter">SNAPCON</h1>
        <p className="text-emerald-500/60 text-[11px] font-black uppercase tracking-[0.4em] mt-4">Enterprise Control Unit</p>
      </div>
      <div className="p-14 space-y-8">
        <div className="space-y-6">
          <div className="space-y-3">
            <label className="text-[10px] font-black text-slate-400 uppercase tracking-[0.2em] pl-1">Credentials</label>
            <input type="text" placeholder="Employee ID" className="w-full px-8 py-5 bg-slate-50 border border-slate-100 rounded-[1.5rem] focus:ring-4 ring-emerald-500/10 focus:bg-white outline-none transition-all font-bold text-slate-700 placeholder:text-slate-300" />
            <input type="password" placeholder="Access Token" className="w-full px-8 py-5 bg-slate-50 border border-slate-100 rounded-[1.5rem] focus:ring-4 ring-emerald-500/10 focus:bg-white outline-none transition-all font-bold text-slate-700 placeholder:text-slate-300" />
          </div>
          <button 
            onClick={onLogin}
            className="w-full py-6 bg-emerald-600 hover:bg-emerald-500 text-white font-black rounded-[1.5rem] transition-all shadow-[0_20px_40px_rgba(16,185,129,0.3)] active:scale-[0.97] uppercase tracking-[0.2em] text-xs"
          >
            Authenticate
          </button>
        </div>
      </div>
    </div>
  </div>
);

const HomePage = ({ lines }) => (
  <div className="max-w-[1400px] mx-auto animate-in fade-in duration-700">
    <div className="flex flex-col lg:flex-row justify-between items-start lg:items-center mb-12 gap-6">
      <div>
        <div className="inline-flex items-center gap-2 bg-emerald-100 px-3 py-1 rounded-lg mb-4">
           <div className="w-2 h-2 bg-emerald-600 rounded-full"></div>
           <span className="text-[10px] font-black text-emerald-700 uppercase tracking-widest">Global Status: Optimal</span>
        </div>
        <h2 className="text-5xl font-black text-slate-900 tracking-tight leading-none">Plant Telemetry</h2>
        <p className="text-slate-500 text-base font-medium mt-4 max-w-xl leading-relaxed">Monitoring real-time production efficiency and node stability across all active manufacturing lines.</p>
      </div>
      <div className="flex gap-4">
        <button className="px-8 py-4 bg-white border border-slate-200 rounded-2xl text-[11px] font-black text-slate-700 hover:bg-slate-50 flex items-center gap-3 shadow-sm transition-all uppercase tracking-widest active:scale-95">
          <FileText size={18} className="text-slate-400" /> Export Logs
        </button>
        <button className="px-8 py-4 bg-[#0a1e1a] text-white rounded-2xl text-[11px] font-black hover:bg-emerald-900 flex items-center gap-3 shadow-xl shadow-slate-900/20 transition-all active:scale-95 uppercase tracking-widest">
          <PlusCircle size={18} className="text-emerald-500" /> New Node
        </button>
      </div>
    </div>

    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 mb-12">
      <StatCard label="OEE Performance" value="94.2%" change="+1.2%" icon={<Zap size={24} />} trend="up" />
      <StatCard label="Shift Output" value="4,500" change="+420" icon={<TrendingUp size={24} />} trend="up" />
      <StatCard label="Active Alerts" value="03" change="-1" icon={<AlertTriangle size={24} />} trend="down" isWarning />
      <StatCard label="Uptime Ratio" value="99.9%" change="MAX" icon={<CheckCircle2 size={24} />} trend="neutral" />
    </div>

    <div className="bg-white rounded-[2.5rem] border border-slate-100 shadow-[0_20px_60px_rgba(15,23,42,0.05)] overflow-hidden">
      <div className="px-10 py-8 border-b border-slate-50 flex justify-between items-center">
        <h3 className="font-black text-slate-800 tracking-wider uppercase text-[11px]">Real-time Telemetry Grid</h3>
        <button className="text-[10px] font-black text-emerald-600 uppercase tracking-widest hover:underline">View All Lines</button>
      </div>
      <div className="overflow-x-auto">
        <table className="w-full text-left">
          <thead className="text-slate-400 text-[10px] uppercase tracking-[0.25em] font-black border-b border-slate-50 bg-slate-50/30">
            <tr>
              <th className="px-10 py-6">Identity</th>
              <th className="px-10 py-6">Status</th>
              <th className="px-10 py-6">Performance</th>
              <th className="px-10 py-6">Gross Output</th>
              <th className="px-10 py-6">Consumption</th>
              <th className="px-10 py-6 text-right">Control</th>
            </tr>
          </thead>
          <tbody className="text-sm divide-y divide-slate-50">
            {lines.map((line) => (
              <tr key={line.id} className="hover:bg-slate-50/80 transition-all group">
                <td className="px-10 py-8 font-black text-slate-900 text-base">{line.id}</td>
                <td className="px-10 py-8">
                  <span className={`inline-flex items-center gap-2 px-4 py-2 rounded-xl text-[10px] font-black uppercase tracking-tight ${
                    line.status === 'Running' ? 'bg-emerald-50 text-emerald-700' : 
                    line.status === 'Warning' ? 'bg-amber-50 text-amber-700' : 'bg-red-50 text-red-700'
                  }`}>
                    <div className={`w-1.5 h-1.5 rounded-full ${
                        line.status === 'Running' ? 'bg-emerald-500 animate-pulse' : 
                        line.status === 'Warning' ? 'bg-amber-500' : 'bg-red-500'
                    }`}></div>
                    {line.status}
                  </span>
                </td>
                <td className="px-10 py-8">
                  <div className="flex items-center gap-5">
                    <div className="w-32 h-2.5 bg-slate-100 rounded-full overflow-hidden border border-slate-200">
                      <div className="h-full bg-emerald-500 transition-all duration-1000 shadow-[0_0_10px_rgba(16,185,129,0.5)]" style={{ width: line.efficiency }}></div>
                    </div>
                    <span className="font-black text-slate-800 text-xs">{line.efficiency}</span>
                  </div>
                </td>
                <td className="px-10 py-8">
                  <span className="font-black text-slate-800 text-base">{line.output.toLocaleString()}</span>
                  <span className="text-[10px] text-slate-400 font-bold uppercase ml-2 tracking-tighter">Units</span>
                </td>
                <td className="px-10 py-8 text-slate-500 font-bold">{line.energy}</td>
                <td className="px-10 py-8 text-right">
                  <button className="p-3 bg-slate-50 text-slate-400 hover:text-emerald-600 hover:bg-emerald-50 rounded-2xl transition-all border border-transparent hover:border-emerald-100 active:scale-90">
                    <BarChart3 size={20} />
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
  <div className="max-w-[1400px] mx-auto animate-in slide-in-from-bottom-4 duration-700">
    <div className="mb-12">
      <h2 className="text-4xl font-black text-slate-900 tracking-tight leading-none">Engineer Dashboard</h2>
      <p className="text-slate-500 text-sm font-medium mt-4">Personalized operational overview for Watanabe San.</p>
    </div>

    <div className="grid grid-cols-1 lg:grid-cols-3 gap-10">
      <div className="lg:col-span-2 space-y-10">
        <div className="bg-white p-12 rounded-[3rem] border border-slate-100 shadow-xl shadow-slate-200/40 relative overflow-hidden">
          <div className="absolute top-0 right-0 w-64 h-64 bg-emerald-500/5 blur-[100px] rounded-full -mr-20 -mt-20"></div>
          <h3 className="font-black text-slate-800 flex items-center gap-4 mb-10 uppercase text-xs tracking-[0.2em] relative z-10">
            <div className="p-2.5 bg-emerald-50 rounded-xl"><CheckCircle2 size={22} className="text-emerald-600" /></div> Assigned Protocols
          </h3>
          <div className="space-y-6 relative z-10">
            <TaskItem title="System Calibration - Line 03" priority="High" deadline="14:00 Today" progress={75} />
            <TaskItem title="Weekly Maintenance Audit" priority="Medium" deadline="Tomorrow" progress={20} />
            <TaskItem title="Inventory Cycle Count" priority="Low" deadline="Friday" progress={0} />
          </div>
        </div>
      </div>

      <div className="space-y-10">
        <div className="bg-[#0a1e1a] text-white p-12 rounded-[3rem] shadow-2xl relative overflow-hidden group">
          <div className="absolute top-0 right-0 p-8 opacity-5 group-hover:scale-125 group-hover:rotate-12 transition-transform duration-700 pointer-events-none">
              <Box size={200} />
          </div>
          <div className="flex flex-col items-center text-center mb-12 relative z-10">
             <div className="w-24 h-24 rounded-[2rem] bg-gradient-to-br from-emerald-400 to-emerald-600 flex items-center justify-center font-black text-4xl mb-6 shadow-2xl shadow-emerald-500/40 italic border-4 border-white/10 ring-1 ring-white/20">W</div>
             <p className="text-2xl font-black tracking-tighter">Watanabe San</p>
             <p className="text-[10px] text-emerald-500 uppercase tracking-[0.4em] font-black mt-3 bg-emerald-500/10 px-4 py-1.5 rounded-full">Senior Lead Engineer</p>
          </div>
          <div className="space-y-6 pt-10 border-t border-white/5 relative z-10">
            <ProfileStat label="Nodes Managed" value="12 Nodes" />
            <ProfileStat label="Uptime Efficiency" value="99.98%" />
            <ProfileStat label="Last Login" value="10m ago" />
          </div>
          <button className="w-full mt-10 py-4 bg-white/5 hover:bg-emerald-500 hover:text-white text-slate-400 font-black rounded-2xl transition-all border border-white/5 text-[10px] uppercase tracking-widest active:scale-95">Edit Profile</button>
        </div>
      </div>
    </div>
  </div>
);

const StatCard = ({ label, value, change, icon, isWarning, trend }) => (
  <div className="bg-white p-10 rounded-[2.5rem] border border-slate-100 shadow-xl shadow-slate-200/30 flex items-start justify-between group hover:border-emerald-200 transition-all hover:-translate-y-2 relative overflow-hidden">
    <div className="absolute top-0 left-0 w-1.5 h-full bg-transparent group-hover:bg-emerald-500 transition-all"></div>
    <div className="relative z-10">
      <p className="text-slate-400 text-[10px] font-black uppercase tracking-[0.2em] mb-4 group-hover:text-emerald-600 transition-colors">{label}</p>
      <h4 className="text-4xl font-black text-slate-900 tracking-tighter mb-4">{value}</h4>
      <p className={`text-[10px] font-black inline-flex items-center gap-2 px-3 py-1.5 rounded-lg ${
        trend === 'up' ? 'bg-emerald-50 text-emerald-600' : 
        trend === 'down' ? 'bg-red-50 text-red-500' : 'bg-slate-100 text-slate-600'
      }`}>
        {change}
      </p>
    </div>
    <div className={`p-6 rounded-[1.75rem] transition-all duration-500 shadow-inner border border-transparent group-hover:scale-110 ${
      isWarning ? 'bg-amber-50 text-amber-500 group-hover:bg-amber-500 group-hover:text-white' : 'bg-slate-50 text-emerald-600 group-hover:bg-emerald-600 group-hover:text-white group-hover:shadow-[0_15px_30px_rgba(16,185,129,0.3)]'
    }`}>
      {icon}
    </div>
  </div>
);

const TaskItem = ({ title, priority, deadline, progress }) => (
  <div className="p-8 bg-slate-50/50 hover:bg-white hover:shadow-[0_20px_40px_rgba(15,23,42,0.08)] transition-all rounded-[2rem] border border-transparent hover:border-slate-100 cursor-pointer group flex flex-col gap-6">
    <div className="flex items-center justify-between">
      <div className="flex items-center gap-6">
        <div className={`w-4 h-4 rounded-full border-4 border-white shadow-sm ${
          priority === 'High' ? 'bg-red-500' : 
          priority === 'Medium' ? 'bg-amber-500' : 'bg-blue-500'
        }`}></div>
        <div>
          <p className="text-lg font-black text-slate-800 group-hover:text-emerald-700 transition-colors leading-none">{title}</p>
          <p className="text-[10px] text-slate-400 font-bold uppercase tracking-widest mt-2">Target: {deadline}</p>
        </div>
      </div>
      <span className={`text-[10px] font-black px-5 py-2 rounded-xl tracking-widest uppercase border ${
         priority === 'High' ? 'bg-red-50 text-red-600 border-red-100' : 'text-slate-500 bg-white border-slate-200'
      }`}>
        {priority}
      </span>
    </div>
    <div className="space-y-2">
      <div className="flex justify-between text-[10px] font-black uppercase tracking-widest text-slate-400">
        <span>Calibration Progress</span>
        <span className="text-emerald-600">{progress}%</span>
      </div>
      <div className="w-full h-2 bg-slate-200/50 rounded-full overflow-hidden p-[1px]">
        <div className="h-full bg-emerald-500 rounded-full transition-all duration-1000 shadow-[0_0_10px_rgba(16,185,129,0.3)]" style={{ width: `${progress}%` }}></div>
      </div>
    </div>
  </div>
);

const ProfileStat = ({ label, value }) => (
  <div className="flex justify-between items-center group/stat">
    <span className="text-slate-500 font-black uppercase tracking-widest text-[10px] group-hover/stat:text-slate-400 transition-colors">{label}</span>
    <span className="font-black text-emerald-400 bg-emerald-400/10 px-4 py-1.5 rounded-xl group-hover/stat:bg-emerald-500 group-hover/stat:text-white transition-all text-xs">{value}</span>
  </div>
);

export default App;
