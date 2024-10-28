#!/bin/bash

echo "Iniciando o deployment do SSDI..."

# Variáveis de ambiente
export FLASK_APP=run.py
export FLASK_ENV=production

# Iniciar o backend
echo "Iniciando o backend..."
cd backend/
source venv/bin/activate
pip install -r requirements.txt
flask run --host=0.0.0.0 --port=5000 &

# Iniciar o frontend
echo "Iniciando o frontend..."
cd ../frontend/
npm install
npm run build
npm start &

# Iniciar o blockchain
echo "Iniciando o blockchain..."
cd ../blockchain/
npm install
ganache-cli --deterministic --port 8545 &
truffle compile
truffle migrate --reset

echo "Deployment concluído."
