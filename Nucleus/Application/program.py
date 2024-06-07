#CAMADA SERVICE
from Domain.Interfaces.IJobsService import IJobsService
from Domain.Interfaces.IServidoresService import IServidoresService
from Domain.Interfaces.IDescricacaoService import IDescricacaoService

from Service.JobService import JobsService
from Service.ServidoresService import ServidoresService
from Service.DescricaoService import DescricaoService

# CAMADA DE BANCO DE DADOS
from Infrastruncture.Data.Repository.Interfaces.IJobsRepository import IJobsRepository
from Infrastruncture.Data.Repository.Interfaces.IServidoresRepository import IServidoresRepository
from Infrastruncture.Data.Repository.Interfaces.IDescricaoRepository import IDescricaoRepository

from Infrastruncture.Data.Repository.JobsRepository import JobsRepository
from Infrastruncture.Data.Repository.ServidoresRepository import ServidoresRepository
from Infrastruncture.Data.Repository.DescricaoRepository import DescricaoRepository


#CONECTION with DATA BASE
from Infrastruncture.Data.Context.dbSession import DbSession

class DependencyContainer:
    def __init__(self):
        __db = DbSession()

        __JOBrepository:IJobsRepository = JobsRepository(__db)
        __ServidorRepository:IServidoresRepository = ServidoresRepository(__db)
        __DescricaoRepository:IDescricaoRepository = DescricaoRepository(__db)

        self.jobService:IJobsService = JobsService(__JOBrepository)
        self.servidorService:IServidoresService = ServidoresService(__ServidorRepository)
        self.descricaoService:IDescricacaoService = DescricaoService(__DescricaoRepository)

        