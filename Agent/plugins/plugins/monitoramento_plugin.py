# INFRA/CROSSCUTTING/plugins/plugins/shutdown_plugin.py
from pluggy import HookimplMarker
from collections import defaultdict
import psutil
import subprocess
import time
import os

hookimpl = HookimplMarker("monitoramento")

@hookimpl
async def consumo_ram():
    """Hook de ver o consumo de ram geral"""
    try:
        memoria = psutil.virtual_memory()
        percentual_usado = memoria.percent
        return percentual_usado
    except Exception as ex:
        raise Exception(str(ex))
    
@hookimpl
async def consumo_cpu():
    """Hook de ver o consumo de CPU geral."""
    try:
        cpu = psutil.cpu_percent(interval=1)
        return cpu
    except Exception as ex:
        raise Exception(str(ex))

@hookimpl
async def consumo_disco():
    """Hook de ver o total consumido dos DISCOS."""
    try:
        discos = psutil.disk_partitions(all=True)
        info_discos = []
        for disco in discos:
            ponto_montagem = disco.mountpoint
            try:
                uso_disco = psutil.disk_usage(ponto_montagem)
                percentual_usado = uso_disco.percent
                livre = uso_disco.free / (1024 * 1024 * 1024)  # Converter bytes para gigabytes
                total = uso_disco.total / (1024 * 1024 * 1024)
                percentual_usado, livre, total = f'{percentual_usado:.2f}%',f'{livre:.2f} GB',f'{total:.2f} GB'
                info_discos.append({
                    "ponto_montagem": ponto_montagem,
                    "percentual_usado": percentual_usado,
                    "livre": livre,
                    "total": total
                })
            except PermissionError:
                # Se não tiver permissão para acessar o disco, continue para o próximo disco
                continue

        return info_discos
    except Exception as ex:
        raise Exception(str(ex))

@hookimpl
async def top_consumo_ram(job_data):
    '''Hook para ver o TOP de RAM'''
    try:
        consumo_memoria = defaultdict(float)
        memoria_total = psutil.virtual_memory().total / (1024 * 1024)  # Converter memória total para MB
        
        for proc in psutil.process_iter(['pid', 'name', 'memory_percent']):
            try:
                pinfo = proc.info
                consumo_memoria[pinfo['name']] += pinfo['memory_percent']
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

        # Ordena os processos pelo percentual de memória utilizada
        consumo_memoria_mb = {nome: (percent / 100) * memoria_total for nome, percent in consumo_memoria.items()}
        
        # Ordenar os processos pelo consumo de memória em MB
        consumo_memoria_mb = sorted(consumo_memoria_mb.items(), key=lambda item: item[1], reverse=True)
        
        # Retornar os top_n processos
        resultado = [(nome, round(memoria, 2)) for nome, memoria in consumo_memoria_mb[:job_data['top_n']]]
        # Arredondar os valores e retornar os top_n processos
        return resultado
    except Exception as ex:
        raise Exception(str(ex))

@hookimpl
async def cmd(job_data):
    '''hook Executa um comando e retorna o resultado'''
    try:
        comando = job_data['comando']
        
        # Verifica se o comando é 'cd' para mudar o diretório de trabalho
        if comando.startswith('cd'):
            novo_diretorio = comando.split(' ')[1]  # Obtém o novo diretório do comando 'cd'
            os.chdir(novo_diretorio)  # Muda o diretório de trabalho do processo principal
            return {"stdout": ["Diretório alterado para", novo_diretorio], "stderr": []}
        
        # Executa outros comandos
        resultado = subprocess.run(comando, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        return {
            "args": resultado.args,
            "returncode": resultado.returncode,
            "stdout": resultado.stdout.splitlines(),
            "stderr": resultado.stderr.splitlines()
        }
    except Exception as ex:
        raise Exception(str(ex))
    