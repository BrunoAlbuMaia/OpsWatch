from pluggy import HookimplMarker
import psutil
import subprocess

hookimpl = HookimplMarker("openClose")


@hookimpl
async def abrir_exe(job_data):
    """Hook de abrir um aplicativo"""
    try:
        subprocess.Popen(job_data['caminho_exe'])
        return 'Executavél aberto com sucesso'
    except FileNotFoundError:
        return ("Nesse caminho não existe esse .exe")
    except Exception as ex:
        return str(ex)

@hookimpl
async def fechar_exe(job_data):
    """Hook de fechar um aplicativo."""
    try:
        lista_executavel = []
        nomeProcesso = job_data['nome_exe']
        for process in psutil.process_iter(attrs=['pid', 'name']):
            if process.info['name'] == nomeProcesso:
                process.terminate()  
                try:
                    process.wait(timeout=5)
                except psutil.TimeoutExpired:
                    process.kill()
                finally:
                    lista_executavel.append(process.info['name'])
            
            #vamos verificar se conseguimos fechar algum executavel
        if len(lista_executavel) == 0:
            raise Exception('Esse executavel não foi encontrado, verique se o nome está escrito corretamente')
        
        return 'Executavél fechado com sucesso'
    except Exception as ex:
        return str(ex)
