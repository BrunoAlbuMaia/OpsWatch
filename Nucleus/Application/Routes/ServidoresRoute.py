from fastapi import APIRouter,WebSocket
from fastapi.responses import JSONResponse
from typing import Dict,Any,List
import asyncio
import websockets

from Domain.Entities.ServidoresEntity import ServidoresEntity
from Application.Controllers.ServidoresController import ServidoresController

router  = APIRouter(tags=['Servidores'])
_controller = ServidoresController()


@router.post('/api/servidor')
async def cadastraServidor(servidor:ServidoresEntity):
    try:
        pass
        return await _controller.registrar(servidor)
    except Exception as ex:
        return JSONResponse(content={'mensagem':str(ex)},status_code=404)