# INFRA/CROSSCUTTING/plugins/plugins/shutdown_plugin.py
from pluggy import HookimplMarker


hookimpl = HookimplMarker("open_close_app")

@hookimpl
async def abrir_exe(job_data):
    """Hook de abrir um aplicativo"""
    print("Abri o Aplicativo que você mandou amigo")
    pass

@hookimpl
async def fechar_exe(job_data):
    """Hook de fechar um aplicativo."""
    print("Fechei o Aplicativo que você mandou amigo")

