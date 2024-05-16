from decouple import config
from typing import Dict,Any

from Domain.Entities.ServidoresEntity import ServidoresEntity
from Infrastruncture.Data.Repository.Interfaces.IServidoresRepository import IServidoresRepository
from Infrastruncture.Data.Context.dbSession import DbSession

class ServidoresRepository(IServidoresRepository):
    def __init__(self,db:DbSession):
        self._db = db

    async def registrar(self, dados: ServidoresEntity):
        cursor = self._db.connect()
        try:
            query = '''
                    INSERT INTO Servidores
                    (nmServidor,nmIpServidor,nmDescricao,urlWebsocketServidor,urlwebSocketJobs)
                    VALUES(?,?,?,?,?)
                    '''
            values = (dados.nmServidor,dados.nmIpServidor,dados.nmDescricao,dados.urlWebsocketServidor,dados.urlWebSocketJobs)

            cursor.execute(query,values)
            self._db.connection.commit()

            return True
        
        except Exception as ex:
            raise Exception(str(ex))
        
        finally:
            self._db.close()
     
    async def atualizar(self, dados: ServidoresEntity):
        try:
            pass
        except Exception as ex:
            raise Exception(str(ex))