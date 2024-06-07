from decouple import config
from typing import Dict,Any

from Domain.Entities.JobsEntity import JobsEntity
from Infrastruncture.Data.Repository.Interfaces.IJobsRepository import IJobsRepository
from Infrastruncture.Data.Context.dbSession import DbSession

class JobsRepository(IJobsRepository):
    def __init__(self,db:DbSession):
        self._db = db

    async def consultarUrl(self, url: str):
        cursor = self._db.connect(as_dict=True)
        try:
            query = '''SELECT jsonConfig FROM Jobs
                        JOIN Servidores as Ser ON
                        Ser.nrServidorId = Jobs.nrServidorId
                        WHERE Ser.urlWebSocketJobs = %s'''
            values = (url,)
            cursor.execute(query,values)
            resultado = cursor.fetchone()
            if resultado == None:
                raise Exception('Não existe essa url')

            return resultado
        except Exception as ex:
            raise Exception(str(ex))
        finally:
            self._db.close()

    async def consultarIp(self,nmIpServidor:str):
        cursor = self._db.connect(as_dict=True)
        try:
            query = '''SELECT jsonConfig FROM Jobs
                        JOIN Servidores as Ser ON
                        Ser.nrServidorId = Jobs.nrServidorId
                        WHERE Ser.nmIpServidor = %s'''
            values = (nmIpServidor,)
            cursor.execute(query,values)
            resultado = cursor.fetchone()
            if resultado == None:
                raise Exception('Não existe essa url')

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
                    WHERE (%s,%s,%s,%s)
                    '''
            values = (dados.nrServidorId,dados.jsonConfig,dados.dtCriacao,dados.usuarioCriacao,)
            cursor.execute(query,values)
            self._db.connection.commit()
            return True
            
        except Exception as ex:
            raise Exception(str(ex))
        finally:
            self._db.close()
    async def atualizar(self, url: str, dados: str,):
        cursor = self._db.connect()
        try:
            query = '''
                    UPDATE Jobs
                    SET jsonConfig = %s,
                    dtAtualizacao = GETDATE(),
                    usuarioAlteracao = %s
                    FROM Jobs as J
                    INNER JOIN Servidores as S ON s.nrServidorId = J.nrServidorId
                    WHERE s.urlWebSocketJobs = %s;
                    '''
            values = (dados,'sisdbIntegrador',url)
            cursor.execute(query,values)
            self._db.connection.commit()
        except Exception as ex:
            raise Exception(str(ex))
        finally:
            self._db.close()