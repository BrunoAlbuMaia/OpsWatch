import json
import re
import time

import pymssql



from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.common.exceptions import TimeoutException,NoAlertPresentException,NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys



class DbSession: 

    def connect(self) -> pymssql.Cursor:
        try:
            self.connection = pymssql.connect(server="srvnagbd01",
                            database="dbfbtotvs",
                            user="sisdbFBTotvs",
                            password="515d3f3t0tv53kp"
                        )
            return self.connection.cursor()
        except Exception as ex:
            return f"Erro ao conectar ao banco de dados: {ex}"

    def close(self) -> None:
        '''Fecha o cursor e desconecta do banco de dados'''
        try:
            self.cursor.close()
            if not self.connection.closed:
                self.connection.close()
        except Exception as ex:
            return f"Erro ao fechar conexão: {ex}"

class contraktorRepository:
    def __init__(self):
        self._dbsession =  DbSession()
        pass
    def exec_proc(self):
        cursor = self._dbsession.connect()
        try:
            query = '''
                        EXEC dbfbtotvs.dbo.pa_GetContratosAssDigitalComBaixaPresencial
                    '''
            cursor.execute(query)
            resultado = cursor.fetchall()
            return resultado

            pass
        except:
            print("erro")
        finally:
            self._dbsession.close()
            
    def atualizar_tabela_controktorLog(self,flBaixado:int,nrContraktorLogID:int):
        cursor = self._dbsession.connect()
        try:
            query ='''
                    UPDATE dbFBTotvs.dbo.ContraktorLog
                    SET flBaixado = %s
                    WHERE nmCodContrato = %s
                    '''
            values = (flBaixado,nrContraktorLogID,)
            cursor.execute(query,values)
            self._dbsession.connection.commit()
            return True
            pass
        except Exception as ex:
            print(ex)







class AutomacaoWeb:
        
    def __openEdge(self):
        options = webdriver.EdgeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--headless')
        options.add_argument('--disable-application-cache')
        options.add_argument('-disable-gpu')
        options.add_argument('--disable-extensions')

        return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()),options=options)
    
    async def __openChrome(self):
        options = webdriver.ChromeOptions()

        # options.add_argument(f'--user-data-dir=C:\\Users\\bruno.maia\\AppData\\Local\\Google\\Chrome\\User Data')
        options.add_argument("--disable-gpu")
        options.add_argument("--start-minimized")
        options.add_argument("--disable-notifications")
        options.add_argument('--no-sandbox')
        
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        return driver

    def __aguardar_visibilidade_elemento(self,xpath:str,driver,timeout:float = 10.0):
        try:
            WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            return True
        except TimeoutException:
            return False
    
    def __verifica_visibilidade_do_elemento(self,xpath:str,driver:webdriver,timeout:float=10.0) -> bool:
        """
        Verifica se o elemento especificado é visível na tela.

        :param xpath: O XPath do elemento.
        :param timeout: O tempo máximo (em segundos) que o Selenium aguardará.
        :return: True se o elemento for visível, False caso contrário.
        """
        try:
            WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            return True
        except TimeoutException:
            return False

    def __verifica_presenca_de_alerta(self,driver:webdriver) -> bool:
        '''
            Esse metódo é responsavel por verificar se tem uma alerta presente na tela.
            
            Caso existe uma alerta, ele retorna TRUE.

            Caso não, ele Retorna FALSE
            '''
        try:
            driver.switch_to.alert
            return True
        except NoAlertPresentException:
            return False

    def __aguardando_presenca_alerta(self,driver:webdriver,timeout:float=30) -> bool:
        try:
            alert = WebDriverWait(driver,timeout).until(EC.alert_is_present())
            return True
        except TimeoutException:
            return False

    def __verificar_elemento_existente(self,driver, xpath):
        try:
            driver.find_element(By.XPATH, xpath)
            return True
        except NoSuchElementException:
            return False

    def __preencher_campo(self,driver,xpath:str,json:str):
        try:
            valor = driver.find_element(By.XPATH, xpath)
            if json.get('apagar','') != '':
                valor.send_keys(Keys.CONTROL + 'a')
                valor.send_keys(Keys.DELETE)


            valor.send_keys(json['valor'])
            if json.get('tecla','') != '':
                if json['tecla'] == 'enter':
                    valor.send_keys(Keys.ENTER)
        except Exception as ex:
            pass

    def __clicar_elemento(self,driver,xpath:str):
        try:
            existe:bool = self.__verificar_elemento_existente(driver,xpath)
            if existe:
                driver.find_element(By.XPATH, xpath).click()
        except Exception as ex:
            raise Exception(str(ex))
   
    
    async def abrir_navegador(self,navegador:str):
        navegador = navegador
        if navegador.lower() == "chrome":
            return await self.__openChrome()
        
        elif navegador.lower() == "edge":
            return self.__openEdge()
        
        else:
            raise ValueError(f"Navegador '{navegador}' não suportado.")
        
    async def executar_automacao(self,driver,dados_json,listas:list =[]):
        self._contraktor = contraktorRepository()
        comandos = dados_json
        for comando in comandos:

            if comando["tipo"] == "navegar":
                driver.get(comando["url"])

            elif comando["tipo"] == "preencher":
                self.__preencher_campo(driver=driver,xpath=comando['xpath'],json=comando)

            elif comando['tipo'] == 'clicar':
                self.__clicar_elemento(driver,comando['xpath'])

            elif comando['tipo'] == 'select':
                select_element = driver.find_element(By.XPATH, comando['xpath'])
                select = Select(select_element)
                options = select.options

                if comando['acao'] == 'maior':
                    maior_valor = float('-inf')
                    for option in options:
                        valor = int(option.get_attribute("value"))
                        if valor > maior_valor:
                            maior_valor = valor

                    select.select_by_value(str(maior_valor))

                elif comando['acao'] == 'menor':
                    menor_valor = float('-inf')
                    for option in options:
                        valor = int(option.get_attribute("value"))
                        if valor < menor_valor:
                            menor_valor = valor

                    select.select_by_value(str(menor_valor))
                
                elif comando['acao'] == 'valor':
                    valor_especifico = comando["valor"]
                    select.select_by_value(valor_especifico)

            elif comando['tipo'] == 'procure_elemento':
                opcoes = driver.find_elements(By.CLASS_NAME, comando['classname'])

                for opcao in opcoes:
                    if opcao.text == comando['valor']:
                        opcao.click()
                        break  
            
            elif comando['tipo'] == 'percorrer_tabela':
                    elementos_i = driver.find_elements(By.XPATH, "//div[contains(@style, 'text-align: center; vertical-align: middle; font-size: 70%')]//i[contains(@class, 'fa fa-times fa-2x')]")
                    self.lista_offlines =[]
                    for elemento in elementos_i:
                        # Navegue até o elemento pai (<tr>) que contém o botão de edição
                        
                        tr_pai = elemento.find_element(By.XPATH, "./ancestor::tr")

                        self.__aguardar_visibilidade_elemento(".//td[@class='edit-delete-table-th ng-scope']//a[contains(@class, 'btn green default')]",driver,timeout=15)
                        # Encontre o botão de edição dentro do elemento pai
                        botao_editar = tr_pai.find_element(By.XPATH, ".//td[@class='edit-delete-table-th ng-scope']//a[contains(@class, 'btn green default')]")
                 
                        ng_click_value = botao_editar.get_attribute("ng-click")
                        match = re.search(r'\d+', ng_click_value)
                        if match:
                            numero_edit = int(match.group())
                            self.lista_offlines.append(numero_edit)
            
            elif comando['tipo'] == 'loop':
                comando_fixo = comando['for']
                clicou = True
                # listas = self.__contraktor.exec_proc()
                for lista in listas:
                    for comando_atual in comando_fixo:
                        comando = comando_atual

                        if comando["tipo"] == "navegar":
                            driver.get(comando["url"])
                        
                        elif comando["tipo"] == "aguardar_visibilidade_elemento":
                            self.__aguardar_visibilidade_elemento(comando["xpath"],driver,timeout=comando['timeout'])

                        elif comando["tipo"] == "preencher":
                            valor = driver.find_element(By.XPATH, comando["xpath"])
                            if comando.get('apagar','') != '':
                                valor.send_keys(Keys.CONTROL + 'a')
                                valor.send_keys(Keys.DELETE)
                            if comando['valor'] == '[lista]':
                                valor.send_keys(lista[1])
    
                            else:
                                valor.send_keys(comando['valor'])

                            if comando.get('tecla','') != '':
                                if comando['tecla'] == 'enter':
                                    valor.send_keys(Keys.ENTER)

                        elif comando['tipo'] == 'clicar':
                            existe:bool = self.__verificar_elemento_existente(driver,comando["xpath"])
                            if existe:
                                driver.find_element(By.XPATH, comando["xpath"]).click()
                            else:
                                clicou = False

                        elif comando['tipo'] =='verifica_visibilidade_do_elemento':
                            Bool = True
                            tentativas = 0
                            if tentativas > 0:
                                while tentativas <= comando['tentativas'] or visivel  == True:
                                    visivel = self.__verifica_visibilidade_do_elemento(comando['xpath'],driver,timeout=comando['timeout'])
                                if visivel == False:
                                    Bool=False
                                tentativas += 1
                            else:
                                while Bool:
                                    visivel = self.__verifica_visibilidade_do_elemento(comando['xpath'],driver,timeout=comando['timeout'])
                                    if visivel == False:
                                        Bool=False
                        elif comando['tipo'] == 'log':
                                self._contraktor.atualizar_tabela_controktorLog(flBaixado=1,nrContraktorLogID=lista[0])
      
            elif comando['tipo'] == 'pecorrer_lista':
                for pecorrendo in self.lista_offlines:
                    if comando["tipo"] == "navegar":
                        driver.get(comando["url"] + pecorrendo)
                    elif comando["tipo"] == "aguardar_visibilidade_elemento":
                        aguardando_elemento = self.__aguardar_visibilidade_elemento(comando["xpath"],driver,timeout=comando['timeout'])
                        if aguardando_elemento:
                            nome_catraca = driver.find_element(By.XPATH,'/html/body/div[4]/div[2]/div/div[2]/div/div/div/div[1]/div/div[2]/div').text
                            ip_catraca = driver.find_element(By.XPATH,'//*[@id="host"]')
                            valor_ip_catraca = ip_catraca.get_attribute('value')
                            print(nome_catraca,valor_ip_catraca)
                            driver.find_element(By.XPATH,'/html/body/div[6]/div/div/div[2]/button').click()
                            
                    
                    elif comando['tipo'] == 'clicar':
                        driver.find_element(By.XPATH, comando["xpath"]).click()

            elif comando["tipo"] == "aguardar_visibilidade_elemento":
                self.__aguardar_visibilidade_elemento(comando["xpath"],driver,timeout=comando['timeout'])

            elif comando['tipo'] =='verifica_visibilidade_do_elemento':
                Bool = True
                while Bool:
                    visivel = self.__verifica_visibilidade_do_elemento(comando['xpath'],driver,timeout=comando['timeout'])
                    if visivel == False:
                        Bool=False
            
            elif comando['tipo'] == 'aguardando_presenca_alerta':
                existeAlerta:bool =self.__aguardando_presenca_alerta(driver=comando['tipo'])
                if existeAlerta:
                    existeAlerta = self.__aguardando_presenca_alerta(driver=comando['tipo'])
                    while existeAlerta:
                        alert = driver.switch_to.alert
                        alert.accept()
                        self.__aguardando_presenca_alerta(driver)
                        existeAlerta = self.__verifica_presenca_de_alerta(driver)
                    return True
                else:
                    return False
            

automacao = AutomacaoWeb()
