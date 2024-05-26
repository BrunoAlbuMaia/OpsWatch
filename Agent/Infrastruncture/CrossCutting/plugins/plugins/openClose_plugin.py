# INFRA/CROSSCUTTING/plugins/plugins/shutdown_plugin.py
from pluggy import HookimplMarker
import psutil
import subprocess
import time



hookimpl = HookimplMarker("openClose")

@hookimpl
async def abrir_exe(job_data):
    """Hook de abrir um aplicativo"""
    try:
            subprocess.Popen(job_data['caminho_exe'])

    except Exception as ex:
        raise Exception(str(ex))
    
    print("Abri o Aplicativo que você mandou amigo")
    pass

@hookimpl
async def fechar_exe(job_data):
    """Hook de fechar um aplicativo."""
    try:
            nomeProcesso = job_data['nome_exe']
            for process in psutil.process_iter(attrs=['pid', 'name']):
                if process.info['name'] == nomeProcesso:
                    process.terminate()  
                    try:
                        process.wait(timeout=5)
                    except psutil.TimeoutExpired:
                        process.kill()
 

    except Exception as ex:
        raise Exception(str(ex))
