import React, { useState } from 'react';
import { 
  LayoutDashboard, 
  Home, 
  BarChart3, 
  Settings, 
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

  // Mock Data สำหรับสายการผลิต
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
      <aside className={`${isSidebarOpen ? 'w-64' : 'w-20'} bg-slate-900 text-white transition-all duration-300 flex flex-col shrink-0`}>
        <div className="p-6 flex items-center gap-3">
          <div className="w-8 h-8 bg-emerald-500 rounded-lg flex items-center justify-center font-bold text-white italic shadow-lg shadow-emerald-500/20">S</div>
          {isSidebarOpen && <span className="font-black text-xl tracking-tighter">SNAPCON</span>}
        </div>

        <nav className="flex-1 mt-2 px-3 space-y-1">
          <NavItem 
            icon={<Home size={20} />} 
            label="Home" 
            active={currentPage === 'Home'} 
            expanded={isSidebarOpen}
            onClick={() => setCurrentPage('Home')}
          />
          <NavItem 
            icon={<LayoutDashboard size={20} />} 
            label="My Dashboard" 
            active={currentPage === 'My Dashboard'} 
            expanded={isSidebarOpen}
            onClick={() => setCurrentPage('My Dashboard')}
          />
          
          {isSidebarOpen && (
            <div className="mt-8 mb-4 px-3">
              <p className="text-[10px] font-bold text-slate-500 uppercase tracking-widest">Resources</p>
              <div className="mt-4 space-y-2">
                <ResourceButton icon={<FileCode size={16} />} label="DWG File" color="bg-emerald-600" />
                <ResourceButton icon={<FileText size={16} />} label="Data Sheet" color="bg-slate-700" />
                <ResourceButton icon={<BookOpen size={16} />} label="Catalog" color="bg-slate-700" />
              </div>
            </div>
          )}
        </nav>

        <div className="p-4 border-t border-slate-800">
          {isSidebarOpen && (
            <div className="mb-4 p-3 bg-slate-800/50 rounded-lg border border-slate-700">
              <p className="text-[10px] text-slate-400 font-bold uppercase">Logged in as:</p>
              <p className="text-sm font-bold text-emerald-400">Watanabe San</p>
              <p className="text-[10px] text-slate-500">Senior Engineer</p>
            </div>
          )}
          <button 
            onClick={() => setIsLoggedIn(false)}
            className="flex items-center gap-4 px-3 py-2 w-full text-slate-400 hover:text-white transition-colors"
          >
            <LogOut size={20} />
            {isSidebarOpen && <span className="text-sm font-medium">Logout</span>}
          </button>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 flex flex-col overflow-hidden">
        {/* Header */}
        <header className="h-16 bg-white border-b border-gray-200 flex items-center justify-between px-6 shrink-0">
          <div className="flex items-center gap-4 text-sm font-medium text-slate-500">
            <button onClick={() => setSidebarOpen(!isSidebarOpen)} className="p-2 hover:bg-gray-100 rounded-lg transition-colors text-slate-400">
              <Menu size={20} />
            </button>
            <span className="text-slate-300">/</span>
            <span>Dashboard</span>
            <span className="text-slate-300">/</span>
            <span className="text-emerald-600 font-bold">{currentPage}</span>
          </div>

          <div className="flex items-center gap-6">
            <div className="relative hidden md:block">
              <Search className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" size={16} />
              <input 
                type="text" 
                placeholder="Search metrics..." 
                className="pl-10 pr-4 py-1.5 bg-gray-100 border-none rounded-full text-sm focus:ring-2 ring-emerald-500/50 w-64 transition-all"
              />
            </div>
            <button className="relative text-slate-400 hover:text-emerald-600 transition-colors">
              <Bell size={20} />
              <span className="absolute -top-1 -right-1 w-4 h-4 bg-red-500 text-white text-[10px] flex items-center justify-center rounded-full border-2 border-white">3</span>
            </button>
            <div className="flex items-center gap-3 pl-4 border-l border-gray-200">
              <div className="w-9 h-9 bg-emerald-500 rounded-full flex items-center justify-center text-white font-bold text-sm shadow-md">
                W
              </div>
            </div>
          </div>
        </header>

        {/* Scrollable Area */}
        <div className="flex-1 overflow-y-auto p-8">
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

// Sub-components
const NavItem = ({ icon, label, active, expanded, onClick }) => (
  <button 
    onClick={onClick}
    className={`
      flex items-center gap-4 px-3 py-3 w-full rounded-lg transition-all
      ${active ? 'bg-emerald-600 text-white shadow-lg shadow-emerald-600/20' : 'text-slate-400 hover:bg-slate-800 hover:text-slate-200'}
    `}
  >
    {icon}
    {expanded && <span className="font-medium text-sm">{label}</span>}
  </button>
);

const ResourceButton = ({ icon, label, color }) => (
  <button className={`w-full flex items-center gap-3 p-3 ${color} hover:opacity-90 transition-all rounded-xl text-white shadow-sm group`}>
    <div className="bg-white/20 p-1.5 rounded-lg group-hover:scale-110 transition-transform">
      {icon}
    </div>
    <span className="text-xs font-bold tracking-tight">{label}</span>
    <Download size={14} className="ml-auto opacity-50" />
  </button>
);

const LoginPage = ({ onLogin }) => (
  <div className="h-screen w-screen bg-slate-950 flex items-center justify-center p-6 relative overflow-hidden">
    {/* Decorative background blur */}
    <div className="absolute top-0 right-0 w-[500px] h-[500px] bg-emerald-600/10 blur-[120px] rounded-full -translate-y-1/2 translate-x-1/2"></div>
    <div className="absolute bottom-0 left-0 w-[500px] h-[500px] bg-blue-600/10 blur-[120px] rounded-full translate-y-1/2 -translate-x-1/2"></div>
    
    <div className="w-full max-w-md bg-white rounded-3xl shadow-2xl overflow-hidden relative z-10">
      <div className="bg-emerald-600 p-10 text-center text-white relative">
        <div className="w-16 h-16 bg-white/20 rounded-2xl mx-auto flex items-center justify-center font-bold text-3xl mb-6 italic shadow-inner">S</div>
        <h1 className="text-2xl font-black tracking-tight">SNAPCON ENTERPRISE</h1>
        <p className="text-emerald-100 text-xs font-bold uppercase tracking-[0.2em] mt-2 opacity-80">Industrial Intelligence v1.5</p>
      </div>
      <div className="p-10">
        <div className="space-y-6">
          <div>
            <label className="block text-[10px] font-black text-slate-400 uppercase tracking-widest mb-2">Username</label>
            <input type="text" placeholder="Enter Staff ID" className="w-full px-5 py-4 bg-gray-50 border border-gray-100 rounded-xl focus:ring-2 ring-emerald-500/20 focus:bg-white outline-none transition-all font-medium" />
          </div>
          <div>
            <label className="block text-[10px] font-black text-slate-400 uppercase tracking-widest mb-2">Password</label>
            <input type="password" placeholder="••••••••" className="w-full px-5 py-4 bg-gray-50 border border-gray-100 rounded-xl focus:ring-2 ring-emerald-500/20 focus:bg-white outline-none transition-all font-medium" />
          </div>
          <button 
            onClick={onLogin}
            className="w-full py-5 bg-emerald-600 hover:bg-emerald-700 text-white font-black rounded-xl transition-all shadow-xl shadow-emerald-600/30 active:scale-[0.98] uppercase tracking-widest text-sm"
          >
            Authenticate
          </button>
        </div>
        <div className="mt-8 flex justify-between items-center text-[10px] font-bold text-slate-400 uppercase tracking-tighter">
            <p>Auth Server: ID-SEA-01</p>
            <p>v1.5.2-STABLE</p>
        </div>
      </div>
    </div>
  </div>
);

const HomePage = ({ lines }) => (
  <div className="max-w-7xl mx-auto">
    <div className="flex flex-col md:flex-row justify-between items-start md:items-end mb-10 gap-4">
      <div>
        <h2 className="text-3xl font-black text-slate-900 tracking-tight">Plant Performance</h2>
        <p className="text-slate-500 text-sm font-medium mt-1">Real-time telemetry and OEE analysis across all active modules.</p>
      </div>
      <div className="flex gap-3">
        <button className="px-5 py-2.5 bg-white border border-gray-200 rounded-xl text-xs font-bold text-slate-700 hover:bg-gray-50 flex items-center gap-2 shadow-sm transition-all">
          <FileText size={16} className="text-slate-400" /> Export PDF Report
        </button>
        <button className="px-5 py-2.5 bg-emerald-600 text-white rounded-xl text-xs font-bold hover:bg-emerald-700 flex items-center gap-2 shadow-lg shadow-emerald-600/20 transition-all active:scale-95">
          <PlusCircle size={16} /> New Monitoring Unit
        </button>
      </div>
    </div>

    {/* Quick Stats */}
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-10">
      <StatCard label="Overall OEE" value="94.2%" change="+1.2%" icon={<Zap className="text-emerald-500" />} />
      <StatCard label="Total Output" value="4,500" change="+420" icon={<TrendingUp className="text-emerald-500" />} />
      <StatCard label="Active Alerts" value="03" change="-1" icon={<AlertTriangle className="text-amber-500" />} isWarning />
      <StatCard label="System Health" value="Stable" change="99.9%" icon={<CheckCircle2 className="text-blue-500" />} />
    </div>

    {/* Production Lines Table */}
    <div className="bg-white rounded-2xl border border-gray-200 shadow-sm overflow-hidden">
      <div className="px-8 py-5 border-b border-gray-100 flex justify-between items-center bg-gray-50/50">
        <h3 className="font-bold text-slate-800 tracking-tight">Live Line Monitoring</h3>
        <div className="flex items-center gap-2">
            <div className="w-2 h-2 bg-emerald-500 rounded-full animate-pulse"></div>
            <span className="text-[10px] font-black text-emerald-600 uppercase tracking-widest">Live Sync</span>
        </div>
      </div>
      <div className="overflow-x-auto">
        <table className="w-full text-left">
          <thead className="text-slate-400 text-[10px] uppercase tracking-[0.15em] font-black border-b border-gray-100">
            <tr>
              <th className="px-8 py-5">Line Identity</th>
              <th className="px-8 py-5">Operational Status</th>
              <th className="px-8 py-5">OEE Score</th>
              <th className="px-8 py-5">Current Output</th>
              <th className="px-8 py-5">Consumption</th>
              <th className="px-8 py-5 text-right">Details</th>
            </tr>
          </thead>
          <tbody className="text-sm divide-y divide-gray-50">
            {lines.map((line) => (
              <tr key={line.id} className="hover:bg-gray-50/80 transition-colors group">
                <td className="px-8 py-5 font-bold text-slate-900">{line.id}</td>
                <td className="px-8 py-5">
                  <span className={`inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-[10px] font-black uppercase tracking-tight ${
                    line.status === 'Running' ? 'bg-emerald-100 text-emerald-700' : 
                    line.status === 'Warning' ? 'bg-amber-100 text-amber-700' : 'bg-red-100 text-red-700'
                  }`}>
                    <div className={`w-1.5 h-1.5 rounded-full ${
                        line.status === 'Running' ? 'bg-emerald-500' : 
                        line.status === 'Warning' ? 'bg-amber-500' : 'bg-red-500'
                    }`}></div>
                    {line.status}
                  </span>
                </td>
                <td className="px-8 py-5">
                  <div className="flex items-center gap-3">
                    <div className="w-24 h-1.5 bg-gray-100 rounded-full overflow-hidden">
                      <div className="h-full bg-emerald-500 transition-all duration-1000" style={{ width: line.efficiency }}></div>
                    </div>
                    <span className="font-bold text-slate-700 text-xs">{line.efficiency}</span>
                  </div>
                </td>
                <td className="px-8 py-5 text-slate-600 font-bold">{line.output.toLocaleString()} <span className="text-[10px] text-slate-400 font-medium">units</span></td>
                <td className="px-8 py-5 text-slate-500 font-medium italic">{line.energy}</td>
                <td className="px-8 py-5 text-right">
                  <button className="text-emerald-600 font-black text-[10px] uppercase tracking-widest hover:text-emerald-700 underline decoration-emerald-500/30 underline-offset-4">View Analytics</button>
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
    <div className="mb-10">
      <h2 className="text-3xl font-black text-slate-900 tracking-tight">Personal Workspace</h2>
      <div className="w-20 h-1.5 bg-emerald-500 mt-4 rounded-full"></div>
    </div>

    <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
      <div className="lg:col-span-2 space-y-8">
        <div className="bg-white p-8 rounded-2xl border border-gray-200 shadow-sm">
          <h3 className="font-black text-slate-800 flex items-center gap-3 mb-6 uppercase text-xs tracking-widest">
            <CheckCircle2 size={18} className="text-emerald-600" /> Pending Approvals
          </h3>
          <div className="space-y-4">
            <TaskItem title="System Calibration - Line 03" priority="High" deadline="Immediate" />
            <TaskItem title="Q4 Inventory Verification" priority="Medium" deadline="Tomorrow" />
            <TaskItem title="New Vendor Compliance" priority="Low" deadline="Friday" />
          </div>
        </div>

        <div className="bg-white p-8 rounded-2xl border border-gray-200 shadow-sm">
            <div className="flex justify-between items-center mb-6">
                <h3 className="font-black text-slate-800 flex items-center gap-3 uppercase text-xs tracking-widest">
                    <BarChart3 size={18} className="text-emerald-600" /> Department Efficiency
                </h3>
                <select className="text-[10px] font-bold bg-gray-50 border-none rounded-lg px-3 py-1 text-slate-500">
                    <option>Last 7 Days</option>
                </select>
            </div>
          <div className="h-56 bg-emerald-50/30 rounded-2xl flex items-end justify-between p-6 gap-3">
            {[45, 65, 40, 95, 85, 70, 90].map((h, i) => (
              <div key={i} className="flex-1 bg-emerald-500 rounded-t-lg hover:bg-emerald-600 transition-all cursor-pointer relative group" style={{ height: `${h}%` }}>
                  <div className="absolute -top-10 left-1/2 -translate-x-1/2 bg-slate-900 text-white text-[10px] px-2 py-1 rounded opacity-0 group-hover:opacity-100 transition-opacity font-bold">
                    {h}%
                  </div>
              </div>
            ))}
          </div>
          <div className="flex justify-between text-[10px] text-slate-400 font-black uppercase mt-4 px-2 tracking-widest">
            <span>Mon</span><span>Tue</span><span>Wed</span><span>Thu</span><span>Fri</span><span>Sat</span><span>Sun</span>
          </div>
        </div>
      </div>

      <div className="space-y-8">
        <div className="bg-slate-900 text-white p-8 rounded-2xl shadow-xl relative overflow-hidden group">
          <div className="absolute top-0 right-0 p-4 opacity-10 group-hover:rotate-12 transition-transform">
              <Box size={100} />
          </div>
          <div className="flex items-center gap-4 mb-8 relative z-10">
             <div className="w-12 h-12 rounded-2xl bg-emerald-500 flex items-center justify-center font-black text-lg shadow-lg shadow-emerald-500/40">W</div>
             <div>
               <p className="text-base font-black tracking-tight">Watanabe San</p>
               <p className="text-[10px] text-emerald-400 uppercase tracking-[0.2em] font-black">Admin Access</p>
             </div>
          </div>
          <div className="space-y-5 pt-6 border-t border-slate-800 relative z-10">
            <ProfileStat label="Active Responsibilities" value="05 Plants" />
            <ProfileStat label="Incident Clearance" value="100%" />
            <ProfileStat label="Department Rank" value="Lead #02" />
          </div>
        </div>

        <div className="bg-white p-8 rounded-2xl border border-gray-200 shadow-sm">
          <h3 className="font-black mb-6 text-slate-800 flex items-center gap-3 text-xs uppercase tracking-widest">
            <Bell size={18} className="text-emerald-600" /> Notifications
          </h3>
          <div className="space-y-4">
            <NotificationItem type="alert" title="Pressure Warning" desc="Drop detected in Line 03 bypass." />
            <NotificationItem type="success" title="Target Reached" desc="Line 01 completed daily quota." />
          </div>
        </div>
      </div>
    </div>
  </div>
);

const StatCard = ({ label, value, change, icon, isWarning }) => (
  <div className="bg-white p-6 rounded-2xl border border-gray-200 shadow-sm flex items-start justify-between group hover:border-emerald-200 transition-colors">
    <div>
      <p className="text-slate-400 text-[10px] font-black uppercase tracking-widest mb-2 group-hover:text-emerald-600 transition-colors">{label}</p>
      <h4 className="text-3xl font-black text-slate-900 tracking-tighter">{value}</h4>
      <p className={`text-[10px] font-black mt-2 inline-flex items-center gap-1 ${isWarning ? 'text-red-500' : 'text-emerald-600'}`}>
        {change} <span className="text-slate-300 font-bold ml-1 tracking-normal">vs Prev.</span>
      </p>
    </div>
    <div className="p-4 bg-gray-50 rounded-2xl group-hover:bg-emerald-50 transition-colors">
      {icon}
    </div>
  </div>
);

const TaskItem = ({ title, priority, deadline }) => (
  <div className="flex items-center justify-between p-4 hover:bg-gray-50 rounded-xl transition-all border border-transparent hover:border-gray-100 cursor-pointer group">
    <div className="flex items-center gap-4">
      <div className={`w-3 h-3 rounded-full shadow-sm ${
        priority === 'High' ? 'bg-red-500' : 
        priority === 'Medium' ? 'bg-amber-500' : 'bg-blue-500'
      }`}></div>
      <div>
        <p className="text-sm font-bold text-slate-700 group-hover:text-emerald-700 transition-colors">{title}</p>
        <p className="text-[10px] text-slate-400 font-bold uppercase tracking-tighter mt-0.5">Deadline: {deadline}</p>
      </div>
    </div>
    <span className={`text-[10px] font-black px-3 py-1 rounded-lg tracking-widest uppercase ${
       priority === 'High' ? 'bg-red-50 text-red-600' : 'text-slate-400 bg-gray-100'
    }`}>
      {priority}
    </span>
  </div>
);

const ProfileStat = ({ label, value }) => (
  <div className="flex justify-between items-center text-xs">
    <span className="text-slate-500 font-bold uppercase tracking-tighter">{label}</span>
    <span className="font-black text-emerald-400">{value}</span>
  </div>
);

const NotificationItem = ({ type, title, desc }) => (
  <div className={`p-4 rounded-xl border-l-4 transition-all hover:translate-x-1 ${
    type === 'alert' ? 'bg-red-50 border-red-500 shadow-red-100' : 'bg-emerald-50 border-emerald-500 shadow-emerald-100'
  } shadow-sm`}>
    <p className={`text-[10px] font-black uppercase tracking-widest ${type === 'alert' ? 'text-red-700' : 'text-emerald-700'}`}>{title}</p>
    <p className="text-xs text-slate-600 font-medium mt-1 leading-relaxed">{desc}</p>
  </div>
);

export default App;
