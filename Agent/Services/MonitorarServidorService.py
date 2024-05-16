import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import win32evtlog  
import win32evtlogutil
import win32con

import time
import requests
import psutil

from Domain.Entites.jobEntity import Job
from Domain.Interface.IMonitorarServidorService import IMonitorarServidorService


class MonitorarServidorService(IMonitorarServidorService):
    
    async def verificar_consumo_ram(self) -> float:
        memoria = psutil.virtual_memory()
        percentual_usado = memoria.percent
        return percentual_usado

    async def verificar_uso_disco(self):
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
    
    async def verificar_consumo_cpu(self):
        cpu_usage = psutil.cpu_percent(interval=1)
        return cpu_usage

    async def verificar_erros_logs(self,server=None, log_type="System", query=None, max_events=10):
        """
        Lê os logs do tipo especificado do Windows.
        
        :param server: nome do servidor para conectar e ler os logs.
        :param log_type: tipo do log (ex. "System", "Application").
        :param query: query para filtrar eventos específicos.
        :param max_events: número máximo de eventos a serem retornados.
        """
        # Abre o log especificado
        hand = win32evtlog.OpenEventLog(server, log_type)
        flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
        total = 0
        
        try:
            log =[]
            while total < max_events:
                # Obtém os eventos do log
                events = win32evtlog.ReadEventLog(hand, flags, 0)
                if not events:  # Se nenhum evento for encontrado, sai do loop
                    break
                
                for event in events:
                    # Exibe informações básicas do evento
                    log.append({"Event ID": {event.EventID}, "Type": {event.EventType}, "Source": {event.SourceName}, "detalhes":{win32evtlogutil.SafeFormatMessage(event, log_type)}})
                    
                    total += 1
                    if total >= max_events:
                        break
                
                return log
        finally:
            win32evtlog.CloseEventLog(hand)

    async def verificar_conectividade(self,url='https://www.google.com/'):
        '''Verifica conectividade com uma URL'''
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                return "Conectividade OK"
            else:
                return "Site acessível, mas resposta inesperada"
        except requests.ConnectionError:
            return "Falha na conectividade"
    
    async def monitorar_processo_especifico(self, nome_processo) -> bool:
        """
        Monitora um processo específico pelo nome.
        """
        # Verifica se o processo está em execução
        for processo in psutil.process_iter(['pid', 'name']):
            if processo.name() == nome_processo:
                return True
        
        # Se o processo não estiver em execução
        return False
