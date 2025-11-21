


import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import logo from './logo.svg';



function App() {
  return (
    <Router>
      <div className="App">
        <nav className="nav-menu mb-4">
          <div className="logo-container">
            <img src={logo} alt="Octofit Tracker Logo" className="App-logo" />
            <Link className="navbar-brand" to="/" style={{ fontSize: '2rem', fontWeight: 'bold', color: '#2575fc', textShadow: '1px 1px 2px #fff' }}>
              Octofit Tracker
            </Link>
          </div>
          <div style={{ flex: 1 }}></div>
          <div>
            <Link className="App-link" to="/activities">Activities</Link>
            <Link className="App-link" to="/leaderboard">Leaderboard</Link>
            <Link className="App-link" to="/teams">Teams</Link>
            <Link className="App-link" to="/users">Users</Link>
            <Link className="App-link" to="/workouts">Workouts</Link>
          </div>
        </nav>
        <div className="container main-content">
          <Routes>
            <Route path="/activities" element={<Activities />} />
            <Route path="/leaderboard" element={<Leaderboard />} />
            <Route path="/teams" element={<Teams />} />
            <Route path="/users" element={<Users />} />
            <Route path="/workouts" element={<Workouts />} />
            <Route path="/" element={<Activities />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}


export default App;
