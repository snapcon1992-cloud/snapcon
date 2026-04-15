import React, { useState, useEffect } from 'react';
import { 
  LayoutDashboard, 
  Home, 
  BarChart3, 
  Settings, 
  LogOut, 
  Bell, 
  Search, 
  User, 
  TrendingUp, 
  Zap, 
  CheckCircle2, 
  AlertTriangle,
  Menu,
  X,
  PlusCircle,
  FileText
} from 'lucide-react';

const App = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [currentPage, setCurrentPage] = useState('Home');
  const [isSidebarOpen, setSidebarOpen] = useState(true);
  const [activeLine, setActiveLine] = useState(null);

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
      <aside className={`${isSidebarOpen ? 'w-64' : 'w-20'} bg-slate-900 text-white transition-all duration-300 flex flex-col`}>
        <div className="p-6 flex items-center gap-3">
          <div className="w-8 h-8 bg-emerald-500 rounded-lg flex items-center justify-center font-bold text-white italic">S</div>
          {isSidebarOpen && <span className="font-black text-xl tracking-tighter">SNAPCON</span>}
        </div>

        <nav className="flex-1 mt-6 px-3">
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
          <NavItem 
            icon={<BarChart3 size={20} />} 
            label="Analytics" 
            active={currentPage === 'Analytics'} 
            expanded={isSidebarOpen}
            onClick={() => setCurrentPage('Analytics')}
          />
          <NavItem 
            icon={<Settings size={20} />} 
            label="Settings" 
            active={currentPage === 'Settings'} 
            expanded={isSidebarOpen}
            onClick={() => setCurrentPage('Settings')}
          />
        </nav>

        <div className="p-4 border-t border-slate-800">
          <button 
            onClick={() => setIsLoggedIn(false)}
            className="flex items-center gap-4 px-3 py-2 w-full text-slate-400 hover:text-white transition-colors"
          >
            <LogOut size={20} />
            {isSidebarOpen && <span>Logout</span>}
          </button>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 flex flex-col overflow-hidden">
        {/* Header */}
        <header className="h-16 bg-white border-b border-gray-200 flex items-center justify-between px-6 shrink-0">
          <div className="flex items-center gap-4 text-sm font-medium text-slate-500">
            <button onClick={() => setSidebarOpen(!isSidebarOpen)} className="p-1 hover:bg-gray-100 rounded">
              <Menu size={20} />
            </button>
            <span className="text-slate-300">/</span>
            <span>Dashboard</span>
            <span className="text-slate-300">/</span>
            <span className="text-slate-900 font-semibold">{currentPage}</span>
          </div>

          <div className="flex items-center gap-6">
            <div className="relative hidden md:block">
              <Search className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" size={16} />
              <input 
                type="text" 
                placeholder="Search resources..." 
                className="pl-10 pr-4 py-1.5 bg-gray-100 border-none rounded-full text-sm focus:ring-2 ring-emerald-500 w-64"
              />
            </div>
            <button className="relative text-slate-600 hover:text-emerald-600">
              <Bell size={20} />
              <span className="absolute -top-1 -right-1 w-4 h-4 bg-red-500 text-white text-[10px] flex items-center justify-center rounded-full border-2 border-white">3</span>
            </button>
            <div className="flex items-center gap-3 pl-4 border-l border-gray-200">
              <div className="text-right hidden sm:block">
                <p className="text-xs font-bold text-slate-900">Watanabe San</p>
                <p className="text-[10px] text-slate-500">Senior Plant Manager</p>
              </div>
              <div className="w-9 h-9 bg-emerald-100 border border-emerald-200 rounded-full flex items-center justify-center text-emerald-700 font-bold">
                W
              </div>
            </div>
          </div>
        </header>

        {/* Scrollable Area */}
        <div className="flex-1 overflow-y-auto p-6">
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
      flex items-center gap-4 px-3 py-3 w-full rounded-lg transition-all mb-1
      ${active ? 'bg-emerald-600 text-white' : 'text-slate-400 hover:bg-slate-800 hover:text-slate-200'}
    `}
  >
    {icon}
    {expanded && <span className="font-medium text-sm">{label}</span>}
  </button>
);

const LoginPage = ({ onLogin }) => (
  <div className="h-screen w-screen bg-slate-900 flex items-center justify-center p-6">
    <div className="w-full max-w-md bg-white rounded-2xl shadow-2xl overflow-hidden">
      <div className="bg-emerald-600 p-8 text-center text-white">
        <div className="w-12 h-12 bg-white/20 rounded-xl mx-auto flex items-center justify-center font-bold text-2xl mb-4 italic">S</div>
        <h1 className="text-2xl font-black tracking-tight">SNAPCON SYSTEMS</h1>
        <p className="text-emerald-100 text-sm opacity-80 uppercase tracking-widest mt-1">Smart Enterprise Solutions</p>
      </div>
      <div className="p-8">
        <div className="mb-6">
          <label className="block text-xs font-bold text-slate-500 uppercase mb-2">Personnel ID</label>
          <input type="text" defaultValue="ADMIN-001" className="w-full px-4 py-3 bg-gray-100 border-none rounded-lg focus:ring-2 ring-emerald-500 outline-none transition-all" />
        </div>
        <div className="mb-8">
          <label className="block text-xs font-bold text-slate-500 uppercase mb-2">Access Key</label>
          <input type="password" defaultValue="••••••••" className="w-full px-4 py-3 bg-gray-100 border-none rounded-lg focus:ring-2 ring-emerald-500 outline-none transition-all" />
        </div>
        <button 
          onClick={onLogin}
          className="w-full py-4 bg-emerald-600 hover:bg-emerald-700 text-white font-bold rounded-lg transition-colors shadow-lg shadow-emerald-600/20"
        >
          LOG IN TO SYSTEM
        </button>
        <p className="text-center text-slate-400 text-xs mt-6">© 2024 SNAPCON ALL RIGHTS RESERVED</p>
      </div>
    </div>
  </div>
);

const HomePage = ({ lines }) => (
  <div className="max-w-7xl mx-auto">
    <div className="flex justify-between items-end mb-8">
      <div>
        <h2 className="text-2xl font-bold text-slate-900">Plant Overview</h2>
        <p className="text-slate-500 text-sm">Real-time status of all production lines across the facility.</p>
      </div>
      <div className="flex gap-2">
        <button className="px-4 py-2 bg-white border border-gray-200 rounded-lg text-sm font-semibold text-slate-700 hover:bg-gray-50 flex items-center gap-2">
          <FileText size={16} /> Export PDF
        </button>
        <button className="px-4 py-2 bg-emerald-600 text-white rounded-lg text-sm font-semibold hover:bg-emerald-700 flex items-center gap-2">
          <PlusCircle size={16} /> New Entry
        </button>
      </div>
    </div>

    {/* Quick Stats */}
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
      <StatCard label="Overall OEE" value="94.2%" change="+1.2%" icon={<Zap className="text-emerald-500" />} />
      <StatCard label="Total Output" value="4,500" change="+420" icon={<TrendingUp className="text-emerald-500" />} />
      <StatCard label="Active Alerts" value="03" change="-1" icon={<AlertTriangle className="text-amber-500" />} isWarning />
      <StatCard label="System Health" value="Stable" change="99.9%" icon={<CheckCircle2 className="text-blue-500" />} />
    </div>

    {/* Production Lines Table */}
    <div className="bg-white rounded-xl border border-gray-200 shadow-sm overflow-hidden">
      <div className="px-6 py-4 border-b border-gray-100 flex justify-between items-center">
        <h3 className="font-bold text-slate-800">Live Production Monitoring</h3>
        <span className="text-xs font-bold text-emerald-600 bg-emerald-50 px-2 py-1 rounded">LIVE UPDATING</span>
      </div>
      <div className="overflow-x-auto">
        <table className="w-full text-left">
          <thead className="bg-gray-50 text-slate-400 text-[10px] uppercase tracking-wider font-bold">
            <tr>
              <th className="px-6 py-4">Line ID</th>
              <th className="px-6 py-4">Status</th>
              <th className="px-6 py-4">OEE Efficiency</th>
              <th className="px-6 py-4">Current Output</th>
              <th className="px-6 py-4">Energy (Real-time)</th>
              <th className="px-6 py-4 text-right">Actions</th>
            </tr>
          </thead>
          <tbody className="text-sm divide-y divide-gray-100">
            {lines.map((line) => (
              <tr key={line.id} className="hover:bg-gray-50 transition-colors">
                <td className="px-6 py-4 font-bold text-slate-700">{line.id}</td>
                <td className="px-6 py-4">
                  <span className={`px-2 py-1 rounded-full text-[10px] font-bold uppercase ${
                    line.status === 'Running' ? 'bg-emerald-100 text-emerald-700' : 
                    line.status === 'Warning' ? 'bg-amber-100 text-amber-700' : 'bg-red-100 text-red-700'
                  }`}>
                    {line.status}
                  </span>
                </td>
                <td className="px-6 py-4">
                  <div className="flex items-center gap-2">
                    <div className="flex-1 h-1.5 bg-gray-100 rounded-full overflow-hidden">
                      <div className="h-full bg-emerald-500" style={{ width: line.efficiency }}></div>
                    </div>
                    <span className="font-bold text-slate-600">{line.efficiency}</span>
                  </div>
                </td>
                <td className="px-6 py-4 text-slate-600 font-medium">{line.output.toLocaleString()} units</td>
                <td className="px-6 py-4 text-slate-500 italic">{line.energy}</td>
                <td className="px-6 py-4 text-right">
                  <button className="text-emerald-600 font-bold text-xs hover:underline">View Details</button>
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
    <div className="mb-8">
      <h2 className="text-2xl font-bold text-slate-900 underline decoration-emerald-500 decoration-4 underline-offset-8">My Dashboard</h2>
      <p className="text-slate-500 text-sm mt-3">Welcome back, Watanabe. Here is your personalized daily performance snapshot.</p>
    </div>

    <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
      {/* Task Summary */}
      <div className="lg:col-span-2 space-y-6">
        <div className="bg-white p-6 rounded-xl border border-gray-200 shadow-sm">
          <h3 className="font-bold mb-4 text-slate-800 flex items-center gap-2">
            <CheckCircle2 size={18} className="text-emerald-600" /> Tasks Assigned to Me
          </h3>
          <div className="space-y-4">
            <TaskItem title="Approve Line 03 Maintenance" priority="High" deadline="Today" />
            <TaskItem title="Review Q3 Sustainability Report" priority="Medium" deadline="Tomorrow" />
            <TaskItem title="Update Safety Protocol (V2.1)" priority="Low" deadline="Fri, 18 Oct" />
          </div>
        </div>

        <div className="bg-white p-6 rounded-xl border border-gray-200 shadow-sm">
          <h3 className="font-bold mb-4 text-slate-800 flex items-center gap-2">
            <BarChart3 size={18} className="text-emerald-600" /> My Performance Trend
          </h3>
          <div className="h-48 bg-emerald-50/50 rounded-lg flex items-end justify-between p-4 gap-2">
            {[40, 60, 45, 90, 80, 75, 95].map((h, i) => (
              <div key={i} className="flex-1 bg-emerald-500 rounded-t-md hover:bg-emerald-600 transition-colors" style={{ height: `${h}%` }}></div>
            ))}
          </div>
          <div className="flex justify-between text-[10px] text-slate-400 font-bold uppercase mt-2 px-2">
            <span>Mon</span><span>Tue</span><span>Wed</span><span>Thu</span><span>Fri</span><span>Sat</span><span>Sun</span>
          </div>
        </div>
      </div>

      {/* Right Column: Personal Stats */}
      <div className="space-y-6">
        <div className="bg-slate-900 text-white p-6 rounded-xl shadow-lg">
          <div className="flex items-center gap-3 mb-6">
             <div className="w-10 h-10 rounded-full bg-emerald-500 flex items-center justify-center font-bold">W</div>
             <div>
               <p className="text-sm font-bold">Watanabe San</p>
               <p className="text-[10px] text-emerald-400 uppercase tracking-widest font-bold">Administrator</p>
             </div>
          </div>
          <div className="space-y-4 pt-4 border-t border-slate-800">
            <div className="flex justify-between text-xs">
              <span className="text-slate-400">Lines Managed</span>
              <span className="font-bold">05 Lines</span>
            </div>
            <div className="flex justify-between text-xs">
              <span className="text-slate-400">Reports Pending</span>
              <span className="font-bold text-amber-400">12 Pending</span>
            </div>
            <div className="flex justify-between text-xs">
              <span className="text-slate-400">Uptime Contribution</span>
              <span className="font-bold text-emerald-400">99.8%</span>
            </div>
          </div>
        </div>

        <div className="bg-white p-6 rounded-xl border border-gray-200 shadow-sm">
          <h3 className="font-bold mb-4 text-slate-800 flex items-center gap-2 text-sm">
            <Bell size={16} className="text-emerald-600" /> Personal Notifications
          </h3>
          <div className="space-y-4">
            <div className="p-3 bg-amber-50 rounded-lg border-l-4 border-amber-400">
              <p className="text-xs font-bold text-amber-900">Urgent Alert</p>
              <p className="text-[10px] text-amber-800 mt-1">Pressure drop detected in Line 03. Please verify.</p>
            </div>
            <div className="p-3 bg-emerald-50 rounded-lg border-l-4 border-emerald-400">
              <p className="text-xs font-bold text-emerald-900">Success</p>
              <p className="text-[10px] text-emerald-800 mt-1">Line 01 daily quota achieved 2 hours early.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
);

const StatCard = ({ label, value, change, icon, isWarning }) => (
  <div className="bg-white p-6 rounded-xl border border-gray-200 shadow-sm flex items-start justify-between">
    <div>
      <p className="text-slate-500 text-[11px] font-bold uppercase tracking-wider mb-2">{label}</p>
      <h4 className="text-3xl font-black text-slate-900 tracking-tight">{value}</h4>
      <p className={`text-[10px] font-bold mt-2 ${isWarning ? 'text-red-500' : 'text-emerald-600'}`}>
        {change} <span className="text-slate-400 font-normal">vs last period</span>
      </p>
    </div>
    <div className="p-3 bg-gray-50 rounded-xl">
      {icon}
    </div>
  </div>
);

const TaskItem = ({ title, priority, deadline }) => (
  <div className="flex items-center justify-between p-3 hover:bg-gray-50 rounded-lg transition-colors border border-transparent hover:border-gray-100">
    <div className="flex items-center gap-3">
      <div className={`w-2 h-2 rounded-full ${
        priority === 'High' ? 'bg-red-500' : 
        priority === 'Medium' ? 'bg-amber-500' : 'bg-blue-500'
      }`}></div>
      <div>
        <p className="text-sm font-semibold text-slate-700">{title}</p>
        <p className="text-[10px] text-slate-400 font-medium italic">Deadline: {deadline}</p>
      </div>
    </div>
    <span className={`text-[10px] font-bold px-2 py-0.5 rounded ${
       priority === 'High' ? 'bg-red-50 text-red-700' : 'text-slate-500 bg-gray-100'
    }`}>
      {priority}
    </span>
  </div>
);

export default App;
