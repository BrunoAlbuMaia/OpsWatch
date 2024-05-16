#CAMADA SERVICE
from Domain.Interfaces.IJobsService import IJobsService
from Domain.Interfaces.IServidoresService import IServidoresService

from Service.JobService import JobsService
from Service.ServidoresService import ServidoresService

# CAMADA DE BANCO DE DADOS
from Infrastruncture.Data.Repository.Interfaces.IJobsRepository import IJobsRepository
from Infrastruncture.Data.Repository.Interfaces.IServidoresRepository import IServidoresRepository

from Infrastruncture.Data.Repository.JobsRepository import JobsRepository
from Infrastruncture.Data.Repository.ServidoresRepository import ServidoresRepository


#CONECTION with DATA BASE
from Infrastruncture.Data.Context.dbSession import DbSession

class DependencyContainer:
    def __init__(self):
        __db = DbSession()

        __JOBrepository:IJobsRepository = JobsRepository(__db)
        __ServidorRepository:IServidoresRepository = ServidoresRepository(__db)

        self.jobService:IJobsService = JobsService(__JOBrepository)
        self.servidorService:IServidoresService = ServidoresService(__ServidorRepository)

        