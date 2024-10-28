# Sistema de Segurança Digital Inteligente (SSDI)

Bem-vindo ao **Sistema de Segurança Digital Inteligente (SSDI)**, uma plataforma inovadora que oferece proteção abrangente contra ameaças cibernéticas, gestão de privacidade e educação em segurança digital para indivíduos e empresas.

## **Visão Geral**

O SSDI é uma solução completa que integra múltiplas camadas de segurança e funcionalidades avançadas, incluindo:

- **Inteligência Preditiva de Ameaças (APT):** Utiliza inteligência artificial e machine learning para prever e antecipar possíveis ameaças, permitindo uma resposta proativa.
- **Proteção de Privacidade Integrada e Otimizada (PPO):** Fornece ferramentas para visualizar, gerir e eliminar rastros digitais, protegendo a privacidade do utilizador.
- **Segurança Holística por Camadas (SHC):** Oferece proteção adaptativa em várias camadas (rede, software, navegação e dispositivos), acompanhando o utilizador em cada ponto de interação digital.
- **Assistente Virtual de Segurança Digital (AVSD):** Um assistente baseado em IA que responde a perguntas, oferece dicas personalizadas e orienta o utilizador na configuração da segurança.
- **Proteção Blockchain para Transações e Identidade Digital:** Integra tecnologia blockchain para proteger transações digitais e identidades, assegurando autenticidade e imutabilidade.
- **Simulador de Ataques e Treino para Colaboradores (SATC):** Um módulo de simulação de ataques cibernéticos que treina colaboradores em como responder a ameaças em tempo real.

## **Índice**

- [Instalação](#instalação)
- [Como Utilizar](#como-utilizar)
- [Arquitetura do Sistema](#arquitetura-do-sistema)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Contribuição](#contribuição)
- [Licença](#licença)
- [Contato](#contato)

## **Instalação/Configuração**
**Configuração do Backend:**
cd backend
python -m venv venv
source venv/bin/activate  # No Windows, use 'venv\Scripts\activate'
pip install -r requirements.txt

**Configuração a base de dados:**
flask db init
flask db migrate
flask db upgrade

**Configuração a base de dados:**
cd ../frontend
npm install

**Configuração do Blockchain:**
cd ../blockchain
npm install

**Iniciar o Ganache CLI:**
ganache-cli --deterministic --port 8545

**Compilar e migre os contratos:**
truffle compile
truffle migrate --reset


### **Pré-requisitos**

- **Python 3.8 ou superior**
- **Node.js 14 ou superior**
- **PostgreSQL**
- **Ganache CLI** (para blockchain local)
- **Truffle**

### **Execução da aplicação**

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/RodrigoCR03/Security_SaaS.git
   cd Security_SaaS

2. **Iniciar o Backend::**
    ```bash
    cd backend
    source venv/bin/activate
    flask run


3. **Iniciar o Frontend::**
    ```bash
    cd frontend
    npm start

4. **Acessar a Aplicação:**
- Abrir o navegador e aceder ao http://localhost:3000


