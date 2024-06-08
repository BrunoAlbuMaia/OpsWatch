from abc import ABCMeta
from typing import Dict,Any
from Infrastruncture.Data.Repository.SqlServer.Interfaces.ICssJobsRepository import ICssJobsRepository
from Infrastruncture.Data.Context.dbSession import DbSession


class CssJobsRepository(ICssJobsRepository):
    def __init__(self,db:DbSession) -> None:
        self._db = db
        return None

    async def consultar(self, nrServidorId: int):
        cursor = self._db.connect(as_dict=True)
        try:
            query = '''
                    SELECT * 
                    FROM cssReplicJobs
                    WHERE nrServidorId = %s
                    '''
            
            values = (nrServidorId,)
            cursor.execute(query,values)
            resultado = cursor.fetchone()

            if resultado == None:
                raise Exception('Não tem registros para replicar')
            
            return resultado
        except Exception as ex:
            raise Exception(str(ex))
        finally:
            self._db.close()

    async def registrar(self,nrServidorId:int,dados:Dict[str,Any]):
        cursor = self._db.connect()
        try:
            query = '''INSERT INTO cssReplicJobs
                        (nrServidorId,jobId)
                        VALUES
                        (%s,%s)'''
            values = (nrServidorId,dados)
            cursor.execute(query,values)
            self._db.commit()
            return True
        except Exception as ex:
            raise Exception(str(ex))
        finally:
            pass

    async def apagar(self, nrServidorId: int, nrJobId: int):
        cursor = self._db.connect()
        try:
            query = '''DELETE FROM cssReplicJobs
                        WHERE nrServidorId = %s
                        AND jobId = %s'''
            values = (nrServidorId,nrJobId)
            cursor.execute(query,values)
            self._db.commit()
            return True
        except Exception as ex:
            raise Exception(str(ex))
        finally:
            self._db.close()
            
