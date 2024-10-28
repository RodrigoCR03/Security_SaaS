import React, { useState } from 'react';
import { registerUser } from '../services/api';
import { useHistory } from 'react-router-dom';

function Register() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const history = useHistory();

  const handleSubmit = e => {
    e.preventDefault();
    registerUser({ name, email, password })
      .then(response => {
        localStorage.setItem('token', response.data.token);
        history.push('/dashboard');
      })
      .catch(error => {
        alert('Erro ao registrar. Tente novamente.');
      });
  };

  return (
    <div className="register-container">
      <h2>Registrar</h2>
      <form onSubmit={handleSubmit}>
        <input type="text" placeholder="Nome" required onChange={e => setName(e.target.value)} />
        <input type="email" placeholder="Email" required onChange={e => setEmail(e.target.value)} />
        <input type="password" placeholder="Senha" required onChange={e => setPassword(e.target.value)} />
        <button type="submit">Registrar</button>
      </form>
    </div>
  );
}

export default Register;
