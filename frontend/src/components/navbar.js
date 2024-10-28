import React from 'react';
import { Link } from 'react-router-dom';
import { Menu } from 'antd';

function Navbar() {
  return (
    <Menu mode="horizontal">
      <Menu.Item key="home">
        <Link to="/">SSDI</Link>
      </Menu.Item>
      <Menu.Item key="dashboard">
        <Link to="/dashboard">Dashboard</Link>
      </Menu.Item>
      <Menu.Item key="privacy">
        <Link to="/privacy">Privacidade</Link>
      </Menu.Item>
      <Menu.Item key="avsd">
        <Link to="/avsd">Assistente Virtual</Link>
      </Menu.Item>
      <Menu.Item key="logout" style={{ float: 'right' }}>
        <Link to="/logout">Sair</Link>
      </Menu.Item>
    </Menu>
  );
}

export default Navbar;
