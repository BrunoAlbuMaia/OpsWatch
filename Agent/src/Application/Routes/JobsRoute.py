from Application.Controllers import JobsController
from fastapi import APIRouter
from typing import Dict,Any


router  = APIRouter(tags=['Jobs'],)

_controller = JobsController()

@router.on_event("startup")
async def start_scheduler():
    try:
        return await _controller.enviar_mensagem_jobs()
    except Exception as ex:
        raise Exception(str(ex))
    
@router.get('/api/jobs',
            summary='Retorna uma lista de todos os jobs cadastrados nesse agente')
async def jobs():
    try:
        return await _controller.jobs()
    except Exception as ex:
        raise Exception(str(ex))

@router.get('/api/jobs/{id}',
            summary='Retorna os detalhes de um job específico com base no seu ID')
async def jobs_id(id:int):
    try:
        return await _controller.jobs_id(id)
    except Exception as ex:
        raise Exception(str(ex))

@router.post('/api/jobs',
            summary='Criar mais um job no seu arquivo de configuração',
            description=''' Nesse Enpoint é possível configurar uma JOB seguindo a estrutura de algum tipo de funcionalidade existente
            por exemplo : JOB de abrir e fechar executaveis, JOB de automacao web, JOB de consumo de APIS
            Caso você passe algo diferente desse padrão não sera possível criar esse job''')       
async def registrar(job:Dict[str,Any]):
    try:
        return await _controller.registrar(job)
    except Exception as ex:
        return Exception(str(ex))

@router.patch('/api/jobs',
            summary='Atualizar dados de um Jobs')
async def atualizar(dados:Dict[str,Any]):
    try:
        resultado = await _controller.atualizar(dados)
        return resultado
    except Exception as ex:
        pass


