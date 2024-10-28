import React from 'react';
import Navbar from '../components/navbar';
import Footer from '../components/footer';
import ThreatList from '../components/threatList';

function Dashboard() {
  return (
    <div>
      <Navbar />
      <div className="container" style={{ padding: '20px' }}>
        <h2>Dashboard</h2>
        <ThreatList />
      </div>
      <Footer />
    </div>
  );
}

export default Dashboard;
