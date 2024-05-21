from decouple import config
from typing import Dict,Any

from Domain.Entities.JobsEntity import JobsEntity
from Infrastruncture.Data.Repository.Interfaces.IJobsRepository import IJobsRepository
from Infrastruncture.Data.Context.dbSession import DbSession

class JobsRepository(IJobsRepository):
    def __init__(self,db:DbSession):
        self._db = db

    async def consultar(self, nrServidorId: int):
        cursor = self._db.connect(as_dict=True)
        try:
            query = '''SELECT jsonConfig FROM Jobs
                        WHERE nrServidorId = ?'''
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
    
    async def registrarJson(self,dados:JobsEntity):
        cursor = self._db.connect()
        try:
            query = '''
                    INSERT INTO 
                    Jobs (nrServidorId,JsonConfig,dtCriacao,usuarioCriacao)
                    WHERE (?,?,?,?)
                    '''
            values = (dados.nrServidorId,dados.jsonConfig,dados.dtCriacao,dados.usuarioCriacao,)
            cursor.execute(query,values)
            self._db.connection.commit()
            return True
            
        except Exception as ex:
            raise Exception(str(ex))
        finally:
            self._db.close()
    async def atualizar(self, nrServidorId: int, dados: Dict[str, Any]):
        try:
            pass
        except Exception as ex:
            raise Exception(str(ex))
        finally:
            self._db.close()