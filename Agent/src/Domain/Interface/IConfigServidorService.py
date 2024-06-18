import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))
from abc import ABC,abstractmethod

from Domain.Entites.jobEntity import Job



class IConfigServidorService(ABC):
    @abstractmethod
    async def consultar_configuracao(self):
        pass

    @abstractmethod
    async def atualizar_configuracao(self,dados:Job):
        pass

    @abstractmethod
    async def configurar_servidor_automaticamente(self):
        pass