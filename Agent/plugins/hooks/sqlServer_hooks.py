from pluggy import HookspecMarker
from Infrastruncture.Data.Context.dbSessionDinamico import DbSessionDinamico

hookimpl = HookspecMarker("sqlServer")
_db = DbSessionDinamico()

@hookimpl
async def select(job_data):
    '''Hooks usado para executar consulta SELECT SQL'''
    pass

@hookimpl
async def execute_query(job_data):
    '''Usada para consultar que tem COMMIT como INSERT, UPDATE ou DELETE'''
    pass

@hookimpl
async def procedure(job_data):
   '''Hooks usado para executar procedures SQL'''
   pass