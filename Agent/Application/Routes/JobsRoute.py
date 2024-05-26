from Application.Controllers.JobsController import JobsController
from Domain.Entites.jobEntity import Job
from fastapi import APIRouter,WebSocket,WebSocketDisconnect
from typing import Dict,Any,List
import asyncio
import json

router  = APIRouter(tags=['Jobs'])

__controller = JobsController()

# Lista para armazenar as conexões dos clientes
connections:List[WebSocket] = []

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    connections.append(websocket)
    last_state = None

    try:
        while True:
            resultado = await __controller.websocket_job(websocket,connections)

            if resultado != last_state:
                last_state = resultado
                for connection in connections:
                    await connection.send_text(str(resultado))
            
            await asyncio.sleep(1)  # Espere 1 segundo antes de enviar a próxima mensagem
    except WebSocketDisconnect:
        print("WebSocket desconectado.")
    except Exception as e:
        print(f"Erro no WebSocket: {e}")
    finally:
        connections.remove(websocket)
  

#ENDPOINTs    
@router.get('/api/jobs',
            summary='Retorna uma lista de todos os jobs cadastrados nesse agente')
async def consultar_jobs_configurados():
   return await __controller.obter_configuration()

@router.get('/api/jobs/{id}',tags=['Jobs'],
            summary='Retorna os detalhes de um job específico com base no seu ID')
async def consultar_jobID(id:int):
    return await __controller.obter_jobs_id(id)

@router.post('/api/jobs',
            summary='Criar mais um job no seu arquivo de configuração',
            description=''' Nesse Enpoint é possível configurar uma JOB seguindo a estrutura de algum tipo de funcionalidade existente
            por exemplo : JOB de abrir e fechar executaveis, JOB de automacao web, JOB de consumo de APIS
            Caso você passe algo diferente desse padrão não sera possível criar esse job''')       
async def inserirJob(job:Dict[str,Any]):
    try:
        return await __controller.cadastrar_job(job)
    except Exception as ex:
        return Exception(str(ex))

@router.patch('/api/jobs',
              summary='Atualiza os dados de um JOB')
async def ataulizar_servico(dados:Dict[str,Any]):
    resultado = await __controller.atualizar_configuration(dados)
    return resultado


