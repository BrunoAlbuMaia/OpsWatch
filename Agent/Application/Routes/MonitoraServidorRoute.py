import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))

from Application.Controllers.MonitorarServidorController import MonitorarServidorController
from Domain.Entites.jobEntity import Job

import asyncio
from typing import Union
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from fastapi import APIRouter,Body,WebSocket
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

router  = APIRouter(tags=['MonitorarServidor'])
__controller = MonitorarServidorController()





@router.websocket('/ws/monitorarServidor')
async def websocket_monitorar_servidor(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            resultado = await __controller.monitoramentoWebSocket(websocket)
            await websocket.send_json(resultado)
            await asyncio.sleep(1)
        except Exception as e:
            print(f"Erro ao enviar dados: {e}")
            break









@router.get(path='/api/monitorarServidor',
            summary='Retorna os status da porcentagem da CPU, MEMORIA RAM, DISCO RIGIDO, LOGS DO SERVIDOR, CONNECTIVIDADE COM A INTERNET',
            responses={
                200:{
                    "content": {
                        "application/json": {
                            "example": {
                                "consumo_ram": "53.9%",
                                "consumo_cpu": "4.2%",
                                "Disco": [
                                    [
                                    {
                                        "ponto_montagem": "C:\\",
                                        "percentual_usado": "28.60%",
                                        "livre": "159.48 GB",
                                        "total": "223.46 GB"
                                    },
                                    {
                                        "ponto_montagem": "D:\\",
                                        "percentual_usado": "6.90%",
                                        "livre": "866.97 GB",
                                        "total": "931.51 GB"
                                    }
                                    ]
                                ],
                                "conectividade": "Conectividade OK"
                            }
                        }
                    }
                }
            })
async def monitorarConsumos():
    try:
        return await __controller.monitorar_recursor()
    except Exception as ex:
        return Exception(str(ex))
    


#CRIAR WEBSOCKET para mostrar dados de monitoramento em tempo real