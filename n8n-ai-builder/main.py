import os
import json
import requests
from dotenv import load_dotenv
from openai import OpenAI
import requests
import os
import re

load_dotenv()

client = OpenAI(api_key=os.getenv("GROQ_API_KEY"))

# 1. Perguntas guiadas
def collect_requirements():
    print("🤖 Vamos montar seu fluxo:\n")

    trigger = input("Qual o gatilho? (webhook/cron): ")
    action = input("O que deseja fazer? (ex: chamar API): ")
    url = input("URL da API (se houver): ")

    return {
        "trigger": trigger,
        "action": action,
        "url": url
    }

# 2. Gerar workflow com IA
# def generate_workflow(data):
#     prompt = f"""
#     Gere um JSON de workflow do n8n com base nisso:
    
#     Trigger: {data['trigger']}
#     Ação: {data['action']}
#     URL: {data['url']}
    
#     Retorne apenas JSON válido no formato do n8n.
#     """

#     response = client.chat.completions.create(
#         model="gpt-4.1-mini",
#         messages=[{"role": "user", "content": prompt}]
#     )

#     content = response.choices[0].message.content

#     try:
#         return json.loads(content)
#     except:
#         print("⚠️ Erro ao parsear JSON, tentando corrigir...")
#         return None



def generate_workflow(data):
    prompt = f"""
    Gere um JSON de workflow do n8n com base nisso:

    Trigger: {data['trigger']}
    Ação: {data['action']}
    URL: {data['url']}

    Retorne APENAS JSON válido.
    NÃO use markdown.
    NÃO explique nada.
    O JSON deve começar com as chaves.
    """

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}",
            "Content-Type": "application/json"
        },
        json={
            "model": "llama-3.1-8b-instant",
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": 0
        }
    )

    data_resp = response.json()

    # 🔍 DEBUG
    if "choices" not in data_resp:
        print("❌ Erro na resposta da API:")
        print(data_resp)
        return None

    content = data_resp["choices"][0]["message"]["content"]

    # 🧹 Remove markdown ```json ... ```
    content = re.sub(r"```json|```", "", content)

    # 🧹 Remove texto antes/depois do JSON
    start = content.find("{")
    end = content.rfind("}") + 1
    content = content[start:end]

    try:
        return json.loads(content)
    except:
        print("❌ JSON inválido gerado:")
        print(content)
        return None
    

def build_workflow(data):
    return {
        "name": "Auto Workflow",
        "nodes": [
            {
                "parameters": {},
                "id": "1",
                "name": "Webhook",
                "type": "n8n-nodes-base.webhook",
                "typeVersion": 1,
                "position": [250, 300]
            },
            {
                "parameters": {
                    "url": data["url"],
                    "options": {}
                },
                "id": "2",
                "name": "HTTP Request",
                "type": "n8n-nodes-base.httpRequest",
                "typeVersion": 1,
                "position": [450, 300]
            }
        ],
        "connections": {
            "Webhook": {
                "main": [
                    [
                        {
                            "node": "HTTP Request",
                            "type": "main",
                            "index": 0
                        }
                    ]
                ]
            }
        },
        "settings": {}
    }

# 3. Enviar para n8n
def send_to_n8n(workflow):
    url = os.getenv("N8N_URL")
    auth = (os.getenv("N8N_USER"), os.getenv("N8N_PASSWORD"))

    response = requests.post(
    url,
    json=workflow,
    headers={
        "X-N8N-API-KEY": os.getenv("N8N_API_KEY"),
        "Content-Type": "application/json"
    }
)

    if response.status_code in [200, 201]:
        print("✅ Workflow criado no n8n!")
    else:
        print("❌ Erro ao enviar:", response.text)


if __name__ == "__main__":
    
    data = collect_requirements()
    workflow = build_workflow(data)

    if workflow:
        send_to_n8n(workflow)
    else:
        print("❌ Falha ao gerar workflow")