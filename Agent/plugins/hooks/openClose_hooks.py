# INFRA/CROSSCUTTING/plugins/hooks.py

import pluggy

hookspec = pluggy.HookspecMarker("openClose")

@hookspec
async def abrir_exe(job_data):
    """Hook de abrir um aplicativo"""
    pass

@hookspec
async def fechar_exe(job_data):
    """Hook de fechar um aplicativo."""
    pass
