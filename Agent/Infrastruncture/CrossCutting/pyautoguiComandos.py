import time
import pyautogui as py

def executar_comandos(comandos):
    acoes = {
        'sleep': lambda cmd: time.sleep(cmd['tempo_segundos']),
        'write': lambda cmd: py.typewrite(cmd['texto']),
        'press': lambda cmd: py.press(cmd['tecla']),
        'click': lambda cmd: py.click(cmd['posicao_x'], cmd['posicao_y']),
        'double_click': lambda cmd: py.doubleClick(cmd['posicao_x'], cmd['posicao_y']),
        'hotkey': lambda cmd: py.hotkey(*cmd['teclas'])
    }
    
    for comando in comandos:
        if 'acao' in comando:
            acao = acoes.get(comando['acao'])
            if acao:
                acao(comando)
        elif 'tempo_segundos' in comando:
            time.sleep(comando['tempo_segundos'])

