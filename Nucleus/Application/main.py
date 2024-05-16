import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from fastapi import FastAPI
import logging
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from Application.Routes.JobsRoute import router as job
from Application.Routes.ServidoresRoute import router as servidor
from datetime import datetime
# Configuração do logger
logging.basicConfig(filename='app.log', level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')
logging.info(f"----------------ULTIMO DEPLOY DO AGENTE {datetime.now()}--------------------------")


app = FastAPI(title="Centralizador de agentes de monitoramento e agendamento de JOBS",
              description="Esse centralizador e responsavel por cuidar dos agentes plugados nos servidores",
              swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"},
              debug=True)

@app.middleware("http")
async def log_requests(request, call_next):
    response = await call_next(request)
    client_ip = request.client.host
    logging.info(f"{request.method} {request.url} - {response.status_code} | IP: {client_ip} ")
    return response


app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(servidor,prefix='/Servidores')
app.include_router(job,prefix='/Jobs')



