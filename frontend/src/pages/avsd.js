import React from 'react';
import Navbar from '../components/navbar';
import Footer from '../components/footer';
import AVSDChat from '../components/avsdchat';

function AVSD() {
  return (
    <div>
      <Navbar />
      <div className="container" style={{ padding: '20px' }}>
        <h2>Assistente Virtual de Segurança Digital</h2>
        <AVSDChat />
      </div>
      <Footer />
    </div>
  );
}

export default AVSD;
