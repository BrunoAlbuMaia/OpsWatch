
from Application.Controllers import ConfigurarServidorController
from Domain.Entites.ConfigServidorEntity import ConfigServidorEntity
from Infrastruncture.CrossCutting.plugins.plugin_manager import PluginManager


from fastapi import APIRouter,WebSocket
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

import asyncio

router  = APIRouter(tags=['Servidor'])
__controller = ConfigurarServidorController()


@router.on_event("startup")
async def start_scheduler():
    return await __controller.configurar_servidor_automaticamente()


@router.websocket('/ws')
async def websocket_monitorar_servidor(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            # resultado = await __controller.monitoramentoWebSocket(websocket)
            await websocket.send_json('resultado')
            await asyncio.sleep(10)
        except Exception as e:
            print(f"Erro ao enviar dados: {e}")
            break
