from fastapi import APIRouter,WebSocket
from fastapi.responses import JSONResponse
from typing import Dict,Any,List
import asyncio
import websockets

from Application.Controllers.JobsController import JobsController

router  = APIRouter(tags=['Jobs'])
__controller = JobsController()


@router.on_event("startup")
async def startup_event():
    await __controller.ativar_consumidorJobs()


@router.get('/api/jobs/{nmIpServidor}')
async def consultarjobs(nmIpServidor:str):
    try:
        return await __controller.consultarIp(nmIpServidor)
    except Exception as ex:
        return JSONResponse(content={'mensagem':str(ex)},status_code=404)

@router.get('/api/jobs/{nmIpServidor}/{jobId}')
async def consultarjobs(nmIpServidor:str,jobId:int):
    try:
        return await __controller.consultarId(nmIpServidor,jobId)
    except Exception as ex:
        return JSONResponse(content={'mensagem':str(ex)},status_code=404)

# @router.post('/api/jobs/{nmIpServidor}')
# async def registrarjobs(nmIpServidor:str,dados:Dict[str,Any]):
#     try:
#         return await __controller.nmIpServidor(nmIpServidor,dados)
#     except Exception as ex:
#         return JSONResponse(content={'mensagem':str(ex)},status_code=404)

@router.patch('/api/jobs/{nmIpServidor}')
async def atualizarjobs(nmIpServidor:str,dados:Dict[str,Any]):
    try:
        return await __controller.atualizarAPI(nmIpServidor,dados)
    except Exception as ex:
        return JSONResponse(content={'mensagem':str(ex)},status_code=404)
