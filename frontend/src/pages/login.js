import React, { useState } from 'react';
import { loginUser } from '../services/api';
import { useHistory } from 'react-router-dom';

function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const history = useHistory();

  const handleSubmit = e => {
    e.preventDefault();
    loginUser({ email, password })
      .then(response => {
        localStorage.setItem('token', response.data.token);
        history.push('/dashboard');
      })
      .catch(error => {
        alert('Credenciais inválidas');
      });
  };

  return (
    <div className="login-container">
      <h2>Entrar</h2>
      <form onSubmit={handleSubmit}>
        <input type="email" placeholder="Email" required onChange={e => setEmail(e.target.value)} />
        <input type="password" placeholder="Senha" required onChange={e => setPassword(e.target.value)} />
        <button type="submit">Entrar</button>
      </form>
    </div>
  );
}

export default Login;
