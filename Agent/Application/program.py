import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#CAMADA SERVICE
from Domain.Interface.IConfigServidorService import IConfigServidorService
from Domain.Interface.IJobsService import IJobsService
from Domain.Interface.IMonitorarServidorService import IMonitorarServidorService
from Domain.Interface.IJobBaseService import IJobBaseService

from Services.MonitorarServidorService import MonitorarServidorService
from Services.ConfigServidorService import ConfigServidorService
from Services.JobsService import JobsService
from Services.AutomacaoWebService import AutomacaoWebService
from Services.JobOpenCloseService import JobOpenCloseService

# CAMADA DE BANCO DE DADOS
from Infrastruncture.Data.Repository.IJobsRepository import IJobsRepository
from Infrastruncture.Data.Repository.JobsRepository import JobsRepository
from Infrastruncture.Data.Repository.IConfigServidorRepository import IConfigServidorRepository
from Infrastruncture.Data.Repository.ConfigServidorRepository import ConfigServidorRepository
from Infrastruncture.Data.Repository.ISQLExecutorRepository import ISQLExecutorRepository
from Infrastruncture.Data.Repository.SQLExecutorRepository import SQLExecutorRepository

#CONECTION with DATA BASE
from Infrastruncture.Data.Context.dbSessionDinamico import DbSessionDinamico

class DependencyContainer:
    def __init__(self):
        __db = DbSessionDinamico()

        __Configrepository:IConfigServidorRepository = ConfigServidorRepository()
        __JOBrepository:IJobsRepository = JobsRepository()
        __SQLRepository:ISQLExecutorRepository = SQLExecutorRepository(__db)
        
        self.jobService:IJobsService = JobsService(__JOBrepository)
        self.configService:IConfigServidorService =  ConfigServidorService(__Configrepository)
        self.monitorarServidorService: IMonitorarServidorService = MonitorarServidorService()

        self.jobOpenClose: IJobBaseService = JobOpenCloseService(__SQLRepository)
        self.automacaoWeb:IJobBaseService = AutomacaoWebService()