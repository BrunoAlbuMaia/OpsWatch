from abc import ABC,abstractmethod

class ISQLExecutorRepository(ABC):
    @abstractmethod
    async def executar_proc(self,nomeProc,parametros:list,conexaoDB) -> None:
        pass