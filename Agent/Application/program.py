import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#CAMADA SERVICE
from Domain.Interface import IConfigServidorService,IJobBaseService,IJobsService,IPluginManagerService
from Services import ConfigServidorService, JobsService, AutomacaoWebService,PluginManagerService

# CAMADA DE BANCO DE DADOS
from Infrastruncture.Data.Repository.Json.Interfaces.IJobsRepository import IJobsRepository
from Infrastruncture.Data.Repository.Json.JobsRepository import JobsRepository
from Infrastruncture.Data.Repository.Json.Interfaces.IConfigServidorRepository import IConfigServidorRepository
from Infrastruncture.Data.Repository.Json.ConfigServidorRepository import ConfigServidorRepository

from Infrastruncture.Data.Repository.RabbitMQ.Interfaces.IRabbitConsumerRepository import IRabbitConsumerRepository
from Infrastruncture.Data.Repository.RabbitMQ.Interfaces.IRabbitPublisherRepository import IRabbitPublisherRepository
from Infrastruncture.Data.Repository.RabbitMQ.RabbitConsumerRepository import RabbitConsumerRepository
from Infrastruncture.Data.Repository.RabbitMQ.RabbitPublisherRepository import RabbitPublisherRepository


#CONECTION with DATA BASE
from Infrastruncture.Data.Context.dbSessionDinamico import DbSessionDinamico
from Infrastruncture.Data.Context.dbSessionRabbit import DbSessionRabbitMQ

class DependencyContainer:
    def __init__(self):
        __db = DbSessionDinamico()
        __rabbit =DbSessionRabbitMQ()

        __Configrepository:IConfigServidorRepository = ConfigServidorRepository()
        __JOBrepository:IJobsRepository = JobsRepository()
        __rabbitConsumerRepository:IRabbitConsumerRepository = RabbitConsumerRepository(__rabbit)
        __rabbitPublishRepository:IRabbitPublisherRepository = RabbitPublisherRepository(__rabbit)

        
        self.jobService:IJobsService = JobsService(__JOBrepository,__rabbitConsumerRepository,__rabbitPublishRepository)
        self.configService:IConfigServidorService =  ConfigServidorService(__Configrepository)



        self.automacaoWeb:IJobBaseService = AutomacaoWebService()
        self.pluginManager:IPluginManagerService = PluginManagerService()