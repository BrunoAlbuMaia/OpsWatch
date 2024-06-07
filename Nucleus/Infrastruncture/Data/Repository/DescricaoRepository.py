from Infrastruncture.Data.Repository.Interfaces.IDescricaoRepository import IDescricaoRepository
from Domain.Entities.DescricaoEntity import DescricaoEntity
from Infrastruncture.Data.Context.dbSession import DbSession

class DescricaoRepository(IDescricaoRepository):
    def __init__(self,db:DbSession) -> None:
        self._db = db

    async def consultar(self):
        cursor = self._db.connect(as_dict=True)
        try:
            query = '''
                    SELECT * 
                    FROM Descriptions
                    '''
            cursor.execute(query)
            resultado  = cursor.fetchall()
            if len(resultado) == 0:
                raise Exception('Não existe dados na tabela')
            return resultado
        except Exception as ex:
            raise Exception(str(ex))
        finally:
            self._db.close()
    
    async def consultar_chave(self, chave: str):
        cursor = self._db.connect(as_dict=True)
        try:
            query = '''
                    SELECT * 
                    FROM Descriptions
                    WHERE nmChavePlugin = %s
                    '''
            values = (chave,)
            cursor.execute(query,values)
            resultado  = cursor.fetchone()
            if resultado == None:
                raise Exception('Essa chave não existe na tabela')
            return resultado
        except Exception as ex:
            raise Exception(str(ex))
        finally:
            self._db.close()
    
    async def registrar(self, descricao: DescricaoEntity):
        cursor = self._db.connect()
        try:
            query = '''
                    INSERT INTO Descriptions(nmChavePlugin,nmJsonPlugin,descricao)
                    VALUES(%s,%s,%s)
                    '''
            values = (descricao.nmChavePlugin,descricao.nmJsonPlugin,descricao.descricao)
            cursor.execute(query,values)
            self._db.connection.commit()
            descricao.nrDescriptionId = cursor.lastrowid

            return descricao
        except Exception as ex:
            raise Exception(str(ex))
        finally:
            self._db.close()
     
    async def atualizar(self, descricao: DescricaoEntity):
        cursor = self._db.connect()
        try:
            query = '''
                    UPDATE
                    Descriptions
                    SET nmChavePlugin = %s,
                    nmJsonPlugin = %s,
                    descricao = %s
                    WHERE nrDescriptionId = %s
                    '''
            values = (descricao.nmChavePlugin,descricao.nmJsonPlugin,descricao.descricao,descricao.nrDescriptionId)
            cursor.execute(query,values)
            self._db.connection.commit()

            return descricao
        except Exception as ex:
            raise Exception(str(ex))
        finally:
            self._db.close()
       
    async def excluir(self,nrDescriptionId:int):
        cursor = self._db.connect()
        try:
            query = '''
                    DELETE FROM Descriptions
                    WHERE nrDescriptionId = %s
                    '''
            cursor.execute(query,(nrDescriptionId,))
            self._db.connection.commit()
            return True
        except Exception as ex:
            raise Exception(str(ex))
        finally:
            self._db.close()
    