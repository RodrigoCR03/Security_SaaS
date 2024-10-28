SSDI/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── models/
│   │   │   ├── user.py
│   │   │   ├── threat.py
│   │   │   ├── privacy.py
│   │   │   ├── avsd.py
│   │   │   └── ... (outros modelos)
│   │   ├── routes/
│   │   │   ├── auth.py
│   │   │   ├── user.py
│   │   │   ├── threat.py
│   │   │   ├── privacy.py
│   │   │   ├── avsd.py
│   │   │   └── ... (outras rotas)
│   │   ├── services/
│   │   │   ├── ai/
│   │   │   │   ├── anomaly_detection.py
│   │   │   │   ├── avsd_service.py
│   │   │   │   └── ... (outros serviços de IA)
│   │   │   ├── blockchain/
│   │   │   │   ├── blockchain_service.py
│   │   │   │   └── ... (outros serviços blockchain)
│   │   │   ├── privacy_service.py
│   │   │   ├── shc_service.py
│   │   │   ├── satc_service.py
│   │   │   └── ... (outros serviços)
│   │   ├── utils/
│   │   │   ├── helpers.py
│   │   │   ├── security.py
│   │   │   └── ... (outras utilidades)
│   │   ├── templates/
│   │   │   └── ... (templates para emails e relatórios)
│   │   ├── static/
│   │   │   └── ... (arquivos estáticos, se necessário)
│   ├── tests/
│   │   ├── test_auth.py
│   │   ├── test_user.py
│   │   ├── test_threat.py
│   │   ├── test_privacy.py
│   │   ├── test_avsd.py
│   │   └── ... (outros testes)
│   ├── requirements.txt
│   ├── run.py
│   └── wsgi.py
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/
│   │   │   ├── Navbar.js
│   │   │   ├── Footer.js
│   │   │   ├── ThreatList.js
│   │   │   ├── PrivacyPanel.js
│   │   │   ├── AVSDChat.js
│   │   │   └── ... (outros componentes)
│   │   ├── pages/
│   │   │   ├── Dashboard.js
│   │   │   ├── Login.js
│   │   │   ├── Register.js
│   │   │   ├── Privacy.js
│   │   │   ├── AVSD.js
│   │   │   └── ... (outras páginas)
│   │   ├── services/
│   │   │   ├── api.js
│   │   │   └── ... (outros serviços)
│   │   ├── reducers/
│   │   │   └── ... (reducers para Redux)
│   │   ├── actions/
│   │   │   └── ... (ações para Redux)
│   │   ├── store.js
│   │   ├── App.js
│   │   └── index.js
│   ├── package.json
│   ├── package-lock.json
│   ├── webpack.config.js
│   └── ... (outros arquivos de configuração)
├── blockchain/
│   ├── contracts/
│   │   ├── IdentityManagement.sol
│   │   ├── TransactionSecurity.sol
│   │   └── ... (outros contratos)
│   ├── migrations/
│   │   ├── 1_initial_migration.js
│   │   ├── 2_deploy_contracts.js
│   │   └── ... (outras migrações)
│   ├── test/
│   │   └── ... (testes para contratos)
│   ├── build/
│   │   └── ... (arquivos compilados)
│   ├── truffle-config.js
│   └── package.json
├── docs/
│   ├── installation_guide.md
│   ├── user_manual.md
│   ├── api_documentation.md
│   ├── technical_specifications.md
│   ├── contribution_guide.md
│   └── ... (outros documentos)
├── scripts/
│   ├── deploy.sh
│   ├── start.sh
│   ├── stop.sh
│   ├── backup.sh
│   └── ... (outros scripts)
├── tests/
│   ├── integration_tests/
│   ├── system_tests/
│   └── ... (outros testes)
├── .gitignore
├── README.md
├── LICENSE
└── ... (outros arquivos na raiz)
