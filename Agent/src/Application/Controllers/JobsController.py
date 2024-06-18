


from ..program import DependencyContainer

class JobsController:
    injection = DependencyContainer()
    def __init__(self) -> None:
        self.jobService = self.injection.jobService

    async def enviar_mensagem_jobs(self):
        #Vamos disparar uma mensagem passando nossas configuracao referente aos JOBS
        return await self.jobService.enviar_mensagem()
    
    async def jobs(self):
        return await self.jobService.jobs()
    
    async def jobs_id(self,id):
        return await self.jobService.job_id(id)
    
    async def registrar(self,entidade):
        try:
            return await self.jobService.registrar(entidade)
        except Exception as ex:
            pass

    async def atualizar(self,dados):
        try:
            return await self.jobService.atualizar(dados)
        except Exception as ex:
            pass




   

    