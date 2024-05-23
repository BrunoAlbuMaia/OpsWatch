from Application.program import DependencyContainer


from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

class JobShedulerController:
    injection = DependencyContainer()
 
    def __init__(self) -> None:
        self.scheduler = AsyncIOScheduler(job_defaults={
        'misfire_grace_time': 15,  # Tempo em segundos para tolerar atrasos na execução
        'coalesce': True,          # Agrupa várias execuções perdidas em uma só para evitar sobrecarga
        'max_instances': 3,        # Limita o número de instâncias simultâneas de um job
        })
        self.jobService = self.injection.jobService
        self.jobOpenClose = self.injection.jobOpenClose
        self.automacaoweb = self.injection.automacaoWeb
        self.plugin_manager_service = self.injection.pluginManager

    async def start(self):
        if not self.scheduler.running:
            self.scheduler.start()
            await self.schedule_job()

    async def schedule_job(self):
        resultado = await self.jobService.consultar_configuracao()
        for res in resultado['jobs']:
            try:
                job_id = res['nomeJOB']
                if res['status'] == True:
                
                    tempo_execucao = str(res['detalhes']["tempExecucao"])
                    
                    existing_job =  self.scheduler.get_job(job_id)
                    if existing_job:
                        self.scheduler.remove_job(job_id)
                    
                    
                    self.scheduler.add_job(
                            self.executarJOB,
                            CronTrigger.from_crontab(tempo_execucao),
                            id=job_id,
                            args=(res,)
                    )
                else:
                    existing_job =  self.scheduler.get_job(job_id)
                    if existing_job:
                        self.scheduler.remove_job(job_id)

            except Exception as ex:
                raise Exception(str(ex))

    
    async def job_agendados(self):
        resultado = self.scheduler.get_jobs()
        if len(resultado) == 0:
            raise Exception("Não tem jobs previsto para serem executados")
        
        jobs = []
        for job in resultado:
            # Formata o próximo horário de execução
            proxima_execucao = job.next_run_time.strftime('%Y-%m-%d %H:%M:%S')

            # Monta um dicionário com os detalhes do job
            job_info = {
                'id': job.id, 
                'proxima_execucao': proxima_execucao,
            }
            jobs.append(job_info)
        
        return jobs

    async def executarJOB(self,res=None,id=None):
        try:
            if res == None:
                res = await self.jobService.consultar_jobs_id(id)
            
            if res['tipo'] == 'chamar_api':
                # await self.jobService.chamar_endpoint(res)
                return 'Não implementado'
            elif res['tipo'] == 'automacao_web':
                # await self.jobService.automacao_contraktor(res)
                await self.automacaoweb.execute_job(job=res)
            else:
                await self.jobOpenClose.execute_job(job=res)
        except Exception as ex:
            raise Exception(str(ex))

    

    async def executar_job_especifico(self, job_data):
        await self.plugin_manager_service.add_plugin_manager('open_close_app')
        result = await self.plugin_manager_service.execute_plugin_hook("open_close_app", "executar_job_especifico", job_data)