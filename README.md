# 🤖 n8n AI Workflow Builder (v1)

Este projeto é um **MVP (v1)** de um construtor de automações utilizando IA, integrado ao n8n.

A ideia é simples:

> O usuário responde algumas perguntas → a IA interpreta → o sistema gera automaticamente um workflow no n8n.

---

## 🚀 Visão do Projeto

Este projeto combina:

* Automação com o n8n
* IA via Groq
* Backend simples em Python

Objetivo:

> Criar uma base para um “Zapier com IA”, onde fluxos são gerados automaticamente a partir de linguagem natural.

---

## ⚠️ Status atual (v1)

Esta é a versão inicial do projeto, com algumas limitações:

* Fluxos ainda são simples (Webhook + HTTP Request)
* IA não gera workflows completos (usa template fixo)
* Sem interface gráfica (CLI apenas)
* Sem validação avançada de fluxos

👉 Mesmo assim, já é um MVP funcional.

---

## 🧠 Como funciona

1. Usuário responde perguntas no terminal:

   * Tipo de gatilho
   * Ação
   * URL

2. IA interpreta (via Groq)

3. Backend monta um workflow válido

4. Workflow é enviado via API para o n8n

5. O fluxo aparece automaticamente no n8n

---

## 📦 Tecnologias utilizadas

* Python 3.10+
* requests
* python-dotenv
* Docker
* n8n
* Groq

---

## ⚙️ Pré-requisitos

Antes de rodar, você precisa ter instalado:

* Docker
* Python 3.10+
* Conta no Groq (para API Key)

---

## 🐳 Subindo o n8n

### 1. Crie a pasta de dados:

```bash
mkdir n8n_data
```

### 2. Crie o arquivo `docker-compose.yml`:

```yaml
version: "3.8"

services:
  n8n:
    image: n8nio/n8n
    ports:
      - "5678:5678"
    environment:
      - N8N_BASIC_AUTH_ACTIVE=true
      - N8N_BASIC_AUTH_USER=admin
      - N8N_BASIC_AUTH_PASSWORD=admin
    volumes:
      - ./n8n_data:/home/node/.n8n
```

### 3. Suba o container:

```bash
docker compose up
```

### 4. Acesse:

```
http://localhost:5678
```

Crie o usuário inicial quando solicitado.

---

## 🔑 Configuração da API Key do n8n

1. Vá em:

   ```
   Settings → API Keys
   ```

2. Gere uma API Key

---

## 🔐 Configuração do projeto

Crie um arquivo `.env`:

```env
GROQ_API_KEY=sua_api_key_groq
N8N_API_KEY=sua_api_key_n8n
N8N_URL=http://localhost:5678/api/v1/workflows
```

---

## 📥 Instalação das dependências

```bash
pip install -r requirements.txt
```

---

## ▶️ Como rodar o projeto

```bash
python main.py
```

---

## 🧪 Exemplo de uso

Você verá perguntas como:

```text
Qual o gatilho? (webhook/cron):
O que deseja fazer? (ex: chamar API):
URL da API:
```

Exemplo:

```text
webhook
chamar API
https://jsonplaceholder.typicode.com/posts/1
```

---

## ✅ Resultado esperado

* Um workflow será criado automaticamente no n8n
* Ele aparecerá no dashboard
* Pronto para execução

---

## 🔥 Próximos passos (v2)

Melhorias planejadas:

* Interface web (React)
* Mais tipos de nodes (IF, banco de dados, email)
* Templates dinâmicos
* Validação automática de workflows
* Melhor uso da IA (decisão de fluxo)

---

## 💡 Ideia futura

Transformar isso em:

> Uma plataforma de automação inteligente (tipo Zapier + IA)

---

## 📌 Observações importantes

* A IA ainda não gera JSON perfeito → usamos templates
* Algumas versões do n8n exigem API Key (não Basic Auth)
* Evite rodar dentro de pastas sincronizadas (ex: OneDrive)

---

## 👨‍💻 Autor

Projeto desenvolvido como MVP para exploração de automação com IA.

---

## 🧠 Licença

Uso livre para estudo e prototipagem.
