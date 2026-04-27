from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv

load_dotenv()
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # libera tudo (ok pra dev)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class WorkflowRequest(BaseModel):
    trigger: str
    action: str
    url: str

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
                "main": [[{
                    "node": "HTTP Request",
                    "type": "main",
                    "index": 0
                }]]
            }
        },
        "settings": {}
    }

@app.post("/generate")
def generate(req: WorkflowRequest):
    workflow = build_workflow(req.dict())

    response = requests.post(
        os.getenv("N8N_URL"),
        json=workflow,
        headers={
            "X-N8N-API-KEY": os.getenv("N8N_API_KEY")
        }
    )

    return {
        "status": "ok",
        "n8n_response": response.json()
    }