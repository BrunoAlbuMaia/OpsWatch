from fastapi import APIRouter,WebSocket
from fastapi.responses import JSONResponse
from typing import Dict,Any,List
import asyncio
import websockets

from Application.Controllers.JobsController import JobsController

router  = APIRouter(tags=['Jobs'])
__controller = JobsController()


# Background task to run the WebSocket client
@router.on_event("startup")
async def startup_event():
    asyncio.create_task(__controller.connect_to_websockets(['ws://localhost:9001/Jobs/ws']))


@router.get('/api/jobs/{nrServidorId}')
async def consultarjobs(nrServidorId:int):
    try:
        return await __controller.consultar(nrServidorId)
    except Exception as ex:
        return JSONResponse(content={'mensagem':str(ex)},status_code=404)

@router.get('/api/jobs/{nrServidorId}/{jobId}')
async def consultarjobs(nrServidorId:int,jobId:int):
    try:
        return await __controller.consultarId(nrServidorId,jobId)
    except Exception as ex:
        return JSONResponse(content={'mensagem':str(ex)},status_code=404)

@router.post('/api/jobs/{nrServidorId}')
async def registrarjobs(nrServidorId:int,dados:Dict[str,Any]):
    try:
        return await __controller.registrar(nrServidorId,dados)
    except Exception as ex:
        return JSONResponse(content={'mensagem':str(ex)},status_code=404)

@router.patch('/api/jobs/{nrServidorId}')
async def atualizarjobs(nrServidorId:int,dados:Dict[str,Any]):
    try:
        return await __controller.atualizar(nrServidorId,dados)
    except Exception as ex:
        return JSONResponse(content={'mensagem':str(ex)},status_code=404)
