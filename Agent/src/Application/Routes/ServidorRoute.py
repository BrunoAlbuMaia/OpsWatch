
from Application.Controllers.ServidorController import ServidorController


from fastapi import APIRouter,WebSocket
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

import asyncio

router  = APIRouter(tags=['Servidor'])
__controller = ServidorController()


@router.on_event("startup")
async def start_scheduler():
    return await __controller.configurar_servidor_automaticamente()


@router.websocket('/ws')
async def websocket_monitorar_servidor(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:

            await websocket.send_json('resultado')
            await asyncio.sleep(10)
        except Exception as e:
            print(f"Erro ao enviar dados: {e}")
            break
