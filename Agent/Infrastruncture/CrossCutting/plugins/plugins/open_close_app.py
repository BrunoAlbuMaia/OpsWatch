# INFRA/CROSSCUTTING/plugins/plugins/shutdown_plugin.py
from pluggy import HookimplMarker
import os

hookimpl = HookimplMarker("open_close_app")

@hookimpl
def abrir_aplicativo(job_data):
    """Hook de abrir um aplicativo"""
    print("Abri o Aplicativo que você mandou amigo")
    pass

@hookimpl
def fechar_aplicativo(job_data):
    """Hook de fechar um aplicativo."""
    print("Fechei o Aplicativo que você mandou amigo")

@hookimpl
def executar_job_especifico(job_data):
    """Hook para executar um job específico."""
    if job_data['acao'] == 'abrir':
        abrir_aplicativo(job_data)
        # Lógica para abrir o aplicativo
    elif job_data['acao'] == 'fechar':
        fechar_aplicativo(job_data)
        # Lógica para fechar o aplicativo
