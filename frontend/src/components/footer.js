import React from 'react';

function Footer() {
  return (
    <footer style={{ textAlign: 'center', marginTop: '20px' }}>
      © {new Date().getFullYear()} SSDI - Todos os direitos reservados.
    </footer>
  );
}

export default Footer;
