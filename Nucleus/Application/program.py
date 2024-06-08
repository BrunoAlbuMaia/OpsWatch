
from Domain import IJobsService,IServidoresService,IDescricacaoService
from Service import JobsService,ServidoresService,DescricaoService
from Infrastruncture import IJobsRepository,IServidoresRepository,IDescricaoRepository,IRabbitPublisherRepository,IRabbitConsumerRepository,JobsRepository,ServidoresRepository,DescricaoRepository,RabbitPublisherRepository,RabbitConsumerRepository
from Infrastruncture import DbSession,DbSessionRabbitMQ

class DependencyContainer:
    def __init__(self):
        __db = DbSession()
        __rabbit = DbSessionRabbitMQ()

        __JOBrepository:IJobsRepository = JobsRepository(__db)
        __ServidorRepository:IServidoresRepository = ServidoresRepository(__db)
        __DescricaoRepository:IDescricaoRepository = DescricaoRepository(__db)
        __rabbitRepository:IRabbitPublisherRepository = RabbitPublisherRepository(__rabbit)
        __rabbitConsumerRepository:IRabbitConsumerRepository = RabbitConsumerRepository(__rabbit)
        self.jobService:IJobsService = JobsService(__JOBrepository,__rabbitConsumerRepository,__rabbitRepository)
        self.servidorService:IServidoresService = ServidoresService(__ServidorRepository)
        self.descricaoService:IDescricacaoService = DescricaoService(__DescricaoRepository)

        