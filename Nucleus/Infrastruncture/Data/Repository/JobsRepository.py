from decouple import config
from typing import Dict,Any


from Infrastruncture.Data.Repository.Interfaces.IJobsRepository import IJobsRepository
from Infrastruncture.Data.Context.dbSession import DbSession

class JobsRepository(IJobsRepository):
    def __init__(self,db:DbSession):
        self._db = db

    async def consultar(self, nrServidorId: int):
        cursor = self._db.connect(as_dict=True)
        try:
            query = '''SELECT * FROM Servidores
                        WHERE nrServidorId = %s'''
            values = (nrServidorId,)
            cursor.execute(query,values)
            resultado = cursor.fetchone()
            if resultado == None:
                raise Exception('Não existe esse nrServidorId')

            return resultado
        except Exception as ex:
            raise Exception(str(ex))
        finally:
            self._db.close()
    
    
    async def atualizar(self, nrServidorId: int, dados: Dict[str, Any]):
        try:
            pass
        except Exception as ex:
            raise Exception(str(ex))