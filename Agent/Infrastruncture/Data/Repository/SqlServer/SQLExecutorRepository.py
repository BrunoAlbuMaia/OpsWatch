import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..','..')))

from Infrastruncture.Data.Repository.SqlServer.Interfaces.ISQLExecutorRepository import ISQLExecutorRepository
from Infrastruncture.Data.Context.dbSessionDinamico import DbSessionDinamico

class SQLExecutorRepository(ISQLExecutorRepository):

    def __init__(self,session:DbSessionDinamico) -> None:
        self.__dbDinamico = session

    async def executar_proc(self,nomeProc,parametros:list,conexaoDB) -> None:
        try:
            cursor = await self.__dbDinamico.connect(conexaoDB)
            query = f"EXEC {nomeProc} "
            values = ()
            # Adiciona os parâmetros à query
            for param in parametros:
                for key, value in param.items():
                    query += f"@{key} = %s, "  # Assume que cada elemento da lista é uma tupla (chave, valor)
                    values += (value,)

            query = query.rstrip(', ')  # Remove a vírgula extra no final
            cursor.execute(query, values)  # Executa a stored procedure com os parâmetros
            resultado = cursor.fetchall() # Retornar o que a procedure devolve
            
            self.__dbDinamico.connection.commit()  # Confirma as alterações no banco de dados
            
            return resultado  # Retorna o resultado da stored procedure, se houver
        
        except Exception as ex:
            return ex.args[0]
    
        finally:
            self.__dbDinamico.close()
