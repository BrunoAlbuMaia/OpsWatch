from fastapi import APIRouter,WebSocket
from fastapi.responses import JSONResponse
from typing import Dict,Any,List
import asyncio
import websockets

from Domain.Entities.ServidoresEntity import ServidoresEntity
from Application.Controllers.ServidoresController import ServidoresController

router  = APIRouter(tags=['Servidores'])
_controller = ServidoresController()


@router.on_event("startup")
async def startup_event():
    asyncio.create_task(_controller.start())

@router.get('/api/servidor/{flAtivo}')
async def consultar_servidores(flAtivo:bool):
    try:
        return JSONResponse(content=await _controller.consultar(flAtivo),status_code=200)
    except Exception as ex:
        return JSONResponse(content={"mensagem":str(ex)})
    
@router.get('/api/servidor')
async def consultar_servidores():
    try:
        return JSONResponse(content=await _controller.consultar(),status_code=200)
    except Exception as ex:
        return JSONResponse(content={"mensagem":str(ex)})

@router.post('/api/servidor')
async def cadastraServidor(servidor:ServidoresEntity):
    try:
        pass
        return await _controller.registrar(servidor)
    except Exception as ex:
        return JSONResponse(content={'mensagem':str(ex)},status_code=404)