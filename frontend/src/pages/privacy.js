import React from 'react';
import Navbar from '../components/navbar';
import Footer from '../components/footer';
import PrivacyPanel from '../components/orivacyPanel';

function Privacy() {
  return (
    <div>
      <Navbar />
      <div className="container" style={{ padding: '20px' }}>
        <h2>Configurações de Privacidade</h2>
        <PrivacyPanel />
      </div>
      <Footer />
    </div>
  );
}

export default Privacy;
