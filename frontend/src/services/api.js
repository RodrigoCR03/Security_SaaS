import axios from 'axios';

const API_URL = '/api';

function getAuthHeaders() {
  const token = localStorage.getItem('token');
  return { 'x-access-token': token };
}

export function registerUser(data) {
  return axios.post(`${API_URL}/auth/register`, data);
}

export function loginUser(data) {
  return axios.post(`${API_URL}/auth/login`, data);
}

export function getThreats() {
  return axios.get(`${API_URL}/threat/list`, { headers: getAuthHeaders() });
}

export function getPrivacySettings() {
  return axios.get(`${API_URL}/privacy/settings`, { headers: getAuthHeaders() });
}

export function updatePrivacySettings(data) {
  return axios.put(`${API_URL}/privacy/settings`, data, { headers: getAuthHeaders() });
}

export function sendMessageToAVSD(data) {
  return axios.post(`${API_URL}/avsd/chat`, data, { headers: getAuthHeaders() });
}

// Outras funções de API conforme necessário
