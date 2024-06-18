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
import json
import re



from Domain.Interface.IJobBaseService import IJobBaseService
from Domain.Entites.AutomacaoWebEntity import AutomacaoWebEntity

class AutomacaoWebService(IJobBaseService):
    def __init__(self) -> None:
        super().__init__()
    
    '''Criar funcionalidades Privadas'''

    async def __openEdge(self):
        options = webdriver.EdgeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--headless')
        options.add_argument('--disable-application-cache')
        options.add_argument('-disable-gpu')
        options.add_argument('--disable-extensions')

        return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()),options=options)
    
    async def __openChrome(self):
        options = webdriver.ChromeOptions()

        options.add_argument("--disable-gpu")
        options.add_argument("--start-minimized")
        options.add_argument("--disable-notifications")
        options.add_argument('--no-sandbox')
        
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        return driver

    async def __aguardar_visibilidade_elemento(self,xpath:str,driver,timeout:float = 10.0):
        try:
            WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            return True
        except TimeoutException:
            return False
    
    async def __verifica_visibilidade_do_elemento(self,xpath:str,driver:webdriver,timeout:float=10.0) -> bool:
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

    async def __verifica_presenca_de_alerta(self,driver:webdriver) -> bool:
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

    async def __aguardando_presenca_alerta(self,driver:webdriver,timeout:float=30) -> bool:
        try:
            alert = WebDriverWait(driver,timeout).until(EC.alert_is_present())
            return True
        except TimeoutException:
            return False

    async def __verificar_elemento_existente(self,driver, xpath):
        try:
            driver.find_element(By.XPATH, xpath)
            return True
        except NoSuchElementException:
            return False

    async def __preencher_campo(self,driver,xpath:str,json:str):
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
            raise Exception(str(ex))

    async def __clicar_elemento(self,driver,xpath:str):
        try:
            existe:bool = self.__verificar_elemento_existente(driver,xpath)
            if existe:
                driver.find_element(By.XPATH, xpath).click()
            else:
                raise Exception('O elemento não está visivel na tela para ser clicado')
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

    async def __select(self,driver,xpath:str,acao:str,valor:str = None):
        try:
            select_element = driver.find_element(By.XPATH, xpath)
            select = Select(select_element)
            options = select.options

            if acao == 'maior':
                maior_valor = float('-inf')
                for option in options:
                    valor = int(option.get_attribute("value"))
                    if valor > maior_valor:
                        maior_valor = valor

                select.select_by_value(str(maior_valor))

            elif acao == 'menor':
                menor_valor = float('-inf')
                for option in options:
                    valor = int(option.get_attribute("value"))
                    if valor < menor_valor:
                        menor_valor = valor

                select.select_by_value(str(menor_valor))
            
            elif acao == 'valor':
                valor_especifico = valor
                select.select_by_value(valor_especifico)
            
            return True
        except Exception as ex:
            return False

    async def __pecorrer_tabela(self,driver,xpath_padrao:str,xpath_generico_tr_pai:str,xpath_botao:str):
        try:
            elementos_i = driver.find_elements(By.XPATH, xpath_padrao)
            self.lista_offlines =[]
            for elemento in elementos_i:
                # Navegue até o elemento pai (<tr>) que contém o botão de edição
                
                tr_pai = elemento.find_element(By.XPATH, xpath_generico_tr_pai)

                self.__aguardar_visibilidade_elemento(xpath_botao,driver,timeout=15)
                # Encontre o botão de edição dentro do elemento pai
                botao_editar = tr_pai.find_element(By.XPATH, xpath_botao)
            
                ng_click_value = botao_editar.get_attribute("ng-click")
                match = re.search(r'\d+', ng_click_value)
                if match:
                    numero_edit = int(match.group())
                    self.lista_offlines.append(numero_edit)
            return True
        except Exception as ex:
            return False
        
    async def __executar_comando(self, driver, comando):
        tipo = comando['tipo']
        if comando["tipo"] == "navegar":
            driver.get(comando["url"])

        elif comando["tipo"] == "preencher":
            await self.__preencher_campo(driver=driver,xpath=comando['xpath'],json=comando)

        elif comando['tipo'] == 'clicar':
            await self.__clicar_elemento(driver,comando['xpath'])

        elif comando['tipo'] == 'select':
           await self.__select(driver,comando['xpath'],comando['acao'],comando['valor'])

        elif comando['tipo'] == 'procure_elemento':
            opcoes = driver.find_elements(By.CLASS_NAME, comando['classname'])

            for opcao in opcoes:
                if opcao.text == comando['valor']:
                    opcao.click()
                    break  
        
        elif comando['tipo'] == 'percorrer_tabela':
            await self.__pecorrer_tabela(driver,
                                        xpath_padrao="//div[contains(@style, 'text-align: center; vertical-align: middle; font-size: 70%')]//i[contains(@class, 'fa fa-times fa-2x')]",
                                        xpath_generico_tr_pai="./ancestor::tr",
                                        xpath_botao=".//td[@class='edit-delete-table-th ng-scope']//a[contains(@class, 'btn green default')]"
                                        )
        
        elif comando["tipo"] == "aguardar_visibilidade_elemento":
                await self.__aguardar_visibilidade_elemento(comando["xpath"],driver,timeout=comando['timeout'])

        elif comando['tipo'] =='verifica_visibilidade_do_elemento':
            Bool = True
            while Bool:
                visivel = await self.__verifica_visibilidade_do_elemento(comando['xpath'],driver,timeout=comando['timeout'])
                if visivel == False:
                    Bool=False
        
    async def __executar_loop(self, driver, comandos):
        for comando in comandos:
            await self.__executar_comando(driver, comando)

    async def execute_job(self, job):
        try:
            automacao_web:AutomacaoWebEntity = AutomacaoWebEntity.parse_obj(job)

            driver = await self.abrir_navegador(automacao_web.detalhes.navegador)

            #vamos seguir os passos que tem dentro de comando_web
            for comando in automacao_web.comandos_web:
                tipo = comando['tipo']
                if tipo == 'loop':
                    await self.__executar_loop(driver, comando['for'])
                else:
                    await self.__executar_comando(driver, comando)


        except Exception as ex:
            return Exception(str(ex))


