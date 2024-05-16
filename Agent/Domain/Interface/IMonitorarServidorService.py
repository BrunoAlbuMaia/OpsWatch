import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))
from abc import ABC,abstractmethod

from Domain.Entites.jobEntity import Job



class IMonitorarServidorService(ABC):
    @abstractmethod
    async def verificar_consumo_ram(self) ->float:
        '''
        Retorna o consumo de ram em formato FLOAT, exemplo:
        50.09
        '''
        pass
    
    @abstractmethod
    async def verificar_uso_disco(self):
        pass
    
    @abstractmethod
    async def verificar_consumo_cpu(self):
        pass

    @abstractmethod
    async def verificar_erros_logs(self,server=None, log_type="System", query=None, max_events=10):
        """
        Lê os logs do tipo especificado do Windows.
        
        :param server: nome do servidor para conectar e ler os logs.
        :param log_type: tipo do log (ex. "System", "Application").
        :param query: query para filtrar eventos específicos.
        :param max_events: número máximo de eventos a serem retornados.
        """
        pass

    @abstractmethod
    async def verificar_conectividade(self,url='https://www.google.com/'):
        pass