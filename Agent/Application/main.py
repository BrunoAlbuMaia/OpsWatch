import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from fastapi import FastAPI
import logging
from fastapi.middleware.cors import CORSMiddleware
from Application.Routes import jobs,jobsSheduler,configServidor,plugin

from datetime import datetime
# Configuração do logger
# logging.basicConfig(filename='app.log', level=logging.INFO)

logging.info(f"----------------ULTIMO DEPLOY DO AGENTE {datetime.now()}--------------------------")

app = FastAPI(title="Serviço de Monitoramento e agendamento de JOBS",
              description="API focada no monitoramento de servidores e agendamento de JOBS",swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"},
              debug=True)

@app.middleware("http")
async def log_requests(request, call_next):
    response = await call_next(request)
    client_ip = request.client.host
    logging.info(f"{request.method} {request.url} - {response.status_code} | IP: {client_ip}")
    return response


app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(configServidor,prefix='/Servidor')
app.include_router(jobs,prefix='/Jobs')
app.include_router(jobsSheduler,prefix='/JobScheduler')
app.include_router(plugin,prefix='/Plugin')


