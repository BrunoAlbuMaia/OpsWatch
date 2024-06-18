#CAMADA SERVICE
from src.Domain import IConfigServidorService, IJobBaseService, IJobsService, IPluginManagerService

from Services import ConfigServidorService, JobsService, AutomacaoWebService,PluginManagerService

# CAMADA DE BANCO DE DADOS
from Infrastruncture.Data.Repository.Json.Interfaces.IJobsRepository import IJobsRepository
from Infrastruncture.Data.Repository.Json.JobsRepository import JobsRepository
from Infrastruncture.Data.Repository.Json.Interfaces.IConfigServidorRepository import IConfigServidorRepository
from Infrastruncture.Data.Repository.Json.ConfigServidorRepository import ConfigServidorRepository


from Infrastruncture.Data.Repository.RabbitMQ.Interfaces.IRabbitPublisherRepository import IRabbitPublisherRepository
from Infrastruncture.Data.Repository.RabbitMQ.RabbitPublisherRepository import RabbitPublisherRepository


#CONECTION with DATA BASE

from Infrastruncture import DbSessionRabbitMQ

class DependencyContainer:
    def __init__(self):

        __rabbit =DbSessionRabbitMQ()

        __Configrepository:IConfigServidorRepository = ConfigServidorRepository()
        __JOBrepository:IJobsRepository = JobsRepository()
        __rabbitPublishRepository:IRabbitPublisherRepository = RabbitPublisherRepository(__rabbit)

        
        self.jobService:IJobsService = JobsService(__JOBrepository,__rabbitPublishRepository)
        self.configService:IConfigServidorService =  ConfigServidorService(__Configrepository)



        self.automacaoWeb:IJobBaseService = AutomacaoWebService()
        self.pluginManager:IPluginManagerService = PluginManagerService()