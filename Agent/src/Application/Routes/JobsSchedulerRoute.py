from Application.Controllers import JobShedulerController
from fastapi import APIRouter
from fastapi.responses import JSONResponse

router  = APIRouter(tags=['JobsScheduler'])
__controller = JobShedulerController()


@router.on_event("startup")
async def start_scheduler():
    return await __controller.start()


@router.get('/api/agendados',
            summary='Verificar os jobs que estão previstos a ser executado')
async def consultar_jobs_agendados():
    try:
        jobs = await __controller.job_agendados()
        return JSONResponse(content=jobs,status_code=200)
    except Exception as ex:
        return JSONResponse(content={"mensagem":str(ex)},status_code=200)


@router.post('/api/executar/{id}',
                summary="Roda um jobs especifico apenas passando o ID")
async def rodarJobID(id:int):
    try:
        resultado = await __controller.executar_job_especifico(id)
        return JSONResponse(content={'mensagem':resultado},status_code=200)
    except Exception as ex:
        return JSONResponse(content={'mensagem':str(ex)},status_code=404)
    

@router.patch('/api/sincronizar',
            summary='Caso tenha feito alguma alteração no seu JOB, execute esse endpoint, ele irá sincronizar as alterações feitas')
async def sincronizar_jobs():
    try:
        await __controller.schedule_job()
        return "Jobs sincronizados com sucesso"
    except Exception as ex:
        return JSONResponse(content={'mensagem':str(ex)},status_code=404)