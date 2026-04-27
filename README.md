# 🤖 n8n AI Workflow Builder (v1)

Este projeto é um **MVP (v1)** de um construtor de automações com IA, integrado ao n8n, com interface conversacional (chat).

> O usuário conversa com a aplicação → responde perguntas → o sistema gera automaticamente um workflow no n8n.

---

## 🚀 Visão do Projeto

O objetivo é construir um sistema onde automações são criadas a partir de linguagem natural, evoluindo para algo similar a um **Zapier com IA**.

Nesta versão, já temos:

* Interface em formato de chatbot 💬
* Backend em API
* Integração com n8n
* Criação automática de workflows

---

## 🧠 Como funciona

1. O usuário interage com o chat (frontend)
2. O sistema faz perguntas guiadas:

   * Gatilho
   * Ação
   * URL
3. O backend processa os dados
4. Um workflow válido é montado via template
5. O workflow é enviado via API para o n8n
6. O fluxo aparece automaticamente no painel do n8n

---

## ⚠️ Status atual (v1)

* Fluxos simples (Webhook → HTTP Request)
* IA ainda não controla toda a estrutura (usa template fixo)
* Sem persistência de dados
* Sem autenticação no frontend

👉 Foco total em validar a ideia

---

## 🏗️ Arquitetura

```text
Frontend (HTML + JS - Chat)
        ↓
Backend (FastAPI)
        ↓
n8n (local via Docker)
```

---

## 📦 Tecnologias utilizadas

* Python 3.10+
* FastAPI
* requests
* python-dotenv
* Docker
* n8n
* Groq

---

## ⚙️ Pré-requisitos

* Docker instalado
* Python 3.10+
* Conta no Groq (API Key)

---

## 🐳 Subindo o n8n

### 1. Crie a pasta:

```bash
mkdir n8n_data
```

---

### 2. docker-compose.yml

```yaml
version: "3.8"

services:
  n8n:
    image: n8nio/n8n
    ports:
      - "5678:5678"
    volumes:
      - ./n8n_data:/home/node/.n8n
```

---

### 3. Suba o serviço

```bash
docker compose up
```

---

### 4. Acesse

http://localhost:5678

Crie o usuário inicial.

---

## 🔑 Configuração do n8n

1. Vá em:

```
Settings → API Keys
```

2. Gere uma API Key

---

## 🔐 Configuração do projeto

Crie um `.env` na raiz:

```env
GROQ_API_KEY=sua_key_groq
N8N_API_KEY=sua_key_n8n
N8N_URL=http://localhost:5678/api/v1/workflows
```

---

## 📥 Instalação

```bash
pip install -r requirements.txt
```

---

## ▶️ Rodando o backend

```bash
uvicorn api:app --reload
```

Acesse:

```
http://localhost:8000/docs
```

---

## 🌐 Rodando o frontend

```bash
python -m http.server 3000
```

Acesse:

```
http://localhost:3000
```

---

## 💬 Como usar

1. Abra o frontend
2. Interaja com o chat
3. Responda as perguntas
4. Aguarde a geração

---

## ✅ Resultado esperado

* Workflow criado automaticamente no n8n
* Visível no painel
* Pronto para execução

---

## ⚠️ Problemas comuns

### ❌ CORS bloqueado

👉 Solução: habilitar CORS no FastAPI

---

### ❌ `N8N_URL = None`

👉 Solução: garantir `load_dotenv()`

---

### ❌ Erro de API Key

👉 Verificar `.env`

---

### ❌ n8n não aceita request

👉 Conferir:

```
/api/v1/workflows ou /rest/workflows
```

---

## 🔥 Próximos passos (v2)

* Chat com IA real (não só steps fixos)
* Suporte a múltiplos tipos de workflow
* Interface mais robusta (React)
* Preview visual do fluxo
* Persistência de histórico
* Deploy em cloud

---

## 💡 Ideia futura

Transformar em:

> Plataforma de automação inteligente baseada em IA

---

## 📌 Observações

* Evite usar pastas com OneDrive (problemas de permissão)
* Não versionar `.env`
* Este projeto é um protótipo funcional

---

## 👨‍💻 Autor

Projeto desenvolvido como MVP para exploração de automação com IA.

---

## 🧠 Licença

Uso livre para estudo e prototipagem.
