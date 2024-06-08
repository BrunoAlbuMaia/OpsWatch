import pluggy

hookspec = pluggy.HookspecMarker("monitoramento")

@hookspec
async def consumo_ram():
    """Hook de ver o consumo de ram geral"""
    pass

@hookspec
async def consumo_cpu():
    """Hook de ver o consumo de CPU geral."""
    pass

@hookspec
async def consumo_disco():
    """Hook de ver o total consumido dos DISCOS."""
    pass

@hookspec
async def top_consumo_ram(job_data):
    '''Hook para ver o TOP de RAM'''
    pass

@hookspec
async def cmd(job_data):
    '''Hook Executa um comando e retorna o resultado'''
    pass