import time
import subprocess
import psutil
import requests
from typing import Type,Dict,Any

from Domain.Entites.jobEntity import Job

from Domain.Interface.IJobsService import IJobsService
from Infrastruncture.Data.Repository.SqlServer.Interfaces.ISQLExecutorRepository import ISQLExecutorRepository
from Infrastruncture.Data.Repository.Json.Interfaces.IJobsRepository import IJobsRepository

from Infrastruncture.Data.Repository.Json.JobsRepository import JobsRepository
from Infrastruncture.Data.Repository.SqlServer.SQLExecutorRepository import SQLExecutorRepository


class JobsService(IJobsService):
    
    def __init__(self,jobRepository: Type[IJobsRepository]) -> None:

        self.__jobRepository = jobRepository
    
    async def consultar_jobs_id(self, id):
        return await self.__jobRepository.get_dados_by_id(job_id=id)
    
    async def consultar_configuracao(self):
        return await self.__jobRepository.get_dados()
    
    async def atualizar_configuracao(self, dados:Dict[str,Any]):
        return await self.__jobRepository.update_dados(dados)
    
    async def inserir_job(self, job:Dict[str,Any]):
        try:
            #Tentar atribuir o json a alguma entidade que temos
            pass
        except Exception as ex:
            pass

    # async def job_open_close(self,res):
    #     try:
    #         job = res
    #         configDB = job['detalhes']['configDB']

    #         # Executa a stored procedure antes de abrir o arquivo
    #         if job['detalhes']['preExecProc'].get('nomeProc','') != '':
    #             resultado_pre_proc = await self.__repository.executar_proc(job['detalhes']['preExecProc']['nomeProc'], 
    #                                     job['detalhes']['preExecProc']['parametros'],
    #                                     configDB)
        
    #         nomeProcesso = job['detalhes']['nomeExecutavel']
    #         caminhoExecutavel = job['detalhes']['caminhoExecutavel']

    #         for process in psutil.process_iter(attrs=['pid', 'name']):
    #             if process.info['name'] == nomeProcesso:
    #                 process.terminate()  
    #                 try:
    #                     process.wait(timeout=5)
    #                     # break
    #                 except psutil.TimeoutExpired:
    #                     process.kill()
            
    #         #Executa uma automação depois de FECHAR o .exe
    #         if len(job['detalhes']['comandos_pos_fechamento'])>0:
    #             executar_comandos(job['detalhes']['comandos_pos_fechamento'])

    #         time.sleep(job['detalhes']['tmpEsperaSegundos'])
    #         subprocess.Popen(caminhoExecutavel)

    #         #Executa uma automação depois de ABRIR o .exe
    #         if len(job['detalhes']['comando_pos_abertura'])>0:
    #             executar_comandos(job['detalhes']['comando_pos_abertura'])

    #         # Executa a stored procedure após abrir o arquivo
    #         if job['detalhes']['posExecProc'].get('nomeProc','') != '':
    #             resultado_pos_proc = await self.__repository.executar_proc(job['detalhes']['postExecProc']['nomeProc'], 
    #                                     job['detalhes']['postExecProc']['parametros'],
    #                                     configDB)
                

    #         print('Monitoramento reiniciado')
    #     except Exception as ex:
    #         raise Exception(str(ex))

    # async def chamar_endpoint(self,res):
    #     headers = res['detalhes']['headers']
    
    #     # Atualiza o cabeçalho Authorization se autenticação OAuth2 for necessária
    #     if res['detalhes']['auth'].get('type') == 'OAuth2':
    #         # token = get_access_token(res['auth'])
    #         headers['Authorization'] = f'Bearer {'token'}'

    #     # Preparando o corpo da requisição
        
    #     if res['detalhes'].get('body','') != '':
    #         if len(res['detalhes']['body']['arquivos']) > 0:
    #             pass
            

    #     match res['detalhes']['metodo_HTTP']:
    #         case 'GET':
    #             response = requests.get(
    #                 res['detalhes']['endpoint'],
    #                 headers=headers,
    #                 timeout=res['detalhes']['timeout']
    #             )
    #             return response.content
    #         case 'POST':
    #             pass
    #         case 'PATCH':
    #             pass
    #         case 'PUT':
    #             pass
    #         case 'DELTE':
    #             pass


    #     # Tratamento da resposta
    #     if response.status_code == 200:
    #         print("Sucesso:", response.content)
    #     else:
    #         print("Falha na requisição:", response.status_code, response.text)

    # async def automacao_contraktor(self,res):
    #     try:
    #         listas = await self.__repository.executar_proc(res['detalhes']['proc']['nome'],res['detalhes']['proc']['parametros'],res['detalhes']['configDB'])
    #         if len(listas) == 0:
    #             raise Exception(str("Não existe contratos para arquivar"))
            
    #         driver = await automacao.abrir_navegador(res['detalhes']['navegador'])
    #         await automacao.executar_automacao(driver,res['comandos_web'],listas)
            
    #     except Exception as ex:
    #         raise Exception(str(ex))
