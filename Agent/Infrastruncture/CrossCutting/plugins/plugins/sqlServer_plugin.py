from pluggy import HookimplMarker
from Infrastruncture.Data.Context.dbSessionDinamico import DbSessionDinamico

hookimpl = HookimplMarker("sqlServer")
_db = DbSessionDinamico()

@hookimpl
async def select(job_data):
    cursor = _db.connect(job_data['connectionString'],as_dict=True)
    try:
        query = job_data['query']
        if '%s' in query:
            values = job_data['values']
            cursor.execute(query,values)
            return cursor.fetchall()     
               
        cursor.execute(query)
        return cursor.fetchall()
    
    except Exception as ex:
        raise Exception(str(ex))
    finally:
        _db.close()

@hookimpl
async def execute_query(job_data):
    '''Usada para consultar que tem COMMIT como INSERT, UPDATE ou DELETE'''
    cursor = _db.connect(job_data['connectionString'])
    try:
        query = job_data['query']
        values = job_data['values']
        cursor.execute(query,values)
        _db.connection.commit()
        return True
    except Exception as ex:
        raise Exception(str(ex))
    finally:
        _db.close()

@hookimpl
async def procedure(job_data):
    cursor = _db.connect(job_data['connectionString'])
    try:
        query = f"EXEC {job_data['procedure']} "
        values = ()
        # Adiciona os parâmetros à query
        for param in job_data['params']:
            for key, value in param.items():
                query += f"@{key} = %s, "  # Assume que cada elemento da lista é uma tupla (chave, valor)
                values += (value,)

        query = query.rstrip(', ')  # Remove a vírgula extra no final
        cursor.execute(query, values)  # Executa a stored procedure com os parâmetros
        resultado = cursor.fetchall() # Retornar o que a procedure devolve
        
        _db.connection.commit()  # Confirma as alterações no banco de dados
        
        return resultado
    
    except Exception as ex:
        raise Exception(str(ex))
    finally:
        _db.close()