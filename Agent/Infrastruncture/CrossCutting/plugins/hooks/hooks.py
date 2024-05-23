# INFRA/CROSSCUTTING/plugins/hooks.py

import pluggy

hookspec = pluggy.HookspecMarker("open_close_app")

@hookspec
async def abrir_aplicativo(job_data):
    """Hook de abrir um aplicativo"""
    pass

@hookspec
async def fechar_aplicativo(job_data):
    """Hook de fechar um aplicativo."""
    pass

@hookspec
async def executar_job_especifico(job_data):
    """Hook para executar um job específico."""
    pass
