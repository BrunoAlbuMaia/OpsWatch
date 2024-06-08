from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import Dict,Any,List

from Domain.Entities.DescricaoEntity import DescricaoEntity

from Application.Controllers.DescricaoController import DescricaoController

router  = APIRouter(tags=['Documentacao'])
__controller = DescricaoController()

@router.get('/api/documentacao')
async def consultardescricao():
    try:
        return await __controller.consultar()
    except Exception as ex:
        return JSONResponse(content={'mensagem':str(ex)},status_code=404)
    
@router.get('/api/documentacao/{nmChavePlugin}')
async def consultar_descricao_chave(nmChavePlugin:str):
    try:
        return await __controller.consultar_chave(nmChavePlugin)
    except Exception as ex:
        return JSONResponse(content={'mensagem':str(ex)},status_code=404)

@router.post('/api/documentacao')
async def registrardescricao(Descricao:DescricaoEntity):
    try:
        pass
        return await __controller.registrar(Descricao)
    except Exception as ex:
        return JSONResponse(content={'mensagem':str(ex)},status_code=404)

@router.patch('/api/documentacao')
async def atualizardescricao(Descricao:DescricaoEntity):
    try:
        return await __controller.atualizar(Descricao)
    except Exception as ex:
        return JSONResponse(content={'mensagem':str(ex)},status_code=404)

@router.delete('/api/documentacao/{nrDescricaoId}')
async def atualizardescricao(nrDescricaoId:int):
    try:
        return await __controller.excluir(nrDescricaoId)
    except Exception as ex:
        return JSONResponse(content={'mensagem':str(ex)},status_code=404)
