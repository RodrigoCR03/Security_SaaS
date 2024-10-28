# Documentação da API

Esta documentação descreve os endpoints da API do SSDI.

## **Autenticação**

### **Registro**

- **Endpoint:** `POST /api/auth/register`
- **Descrição:** Registra um novo utilizador.
- **Parâmetros:**
  - `email` (string) - obrigatório
  - `password` (string) - obrigatório
  - `name` (string) - opcional
- **Exemplo de Requisição:**

```json
{
  "email": "user@example.com",
  "password": "password123",
  "name": "User Name"
}


### **3.4. technical_specifications.md**

```markdown
# Especificações Técnicas

Este documento detalha a arquitetura e as especificações técnicas do SSDI.

## **Arquitetura Geral**

*(Inclua diagramas de arquitetura, descrição dos componentes, fluxos de dados, etc.)*

## **Componentes Principais**

- **Backend:**
  - Linguagem: Python
  - Framework: Flask
  - Banco de Dados: PostgreSQL
- **Frontend:**
  - Linguagem: JavaScript
  - Biblioteca: React.js
- **Blockchain:**
  - Plataforma: Ethereum (Ganache para desenvolvimento)
  - Contratos Inteligentes: Solidity
- **Inteligência Artificial:**
  - Bibliotecas: TensorFlow, PyTorch, Transformers

## **Detalhes de Implementação**

### **1. Inteligência Preditiva de Ameaças**

*(Descreva os algoritmos utilizados, modelos de machine learning, datasets, etc.)*

### **2. Proteção de Privacidade**

*(Descreva como as ferramentas de privacidade foram implementadas.)*

*(Continue detalhando cada funcionalidade.)*

