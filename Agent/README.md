# Agent

- [Como rodar o agente pela primeira vez ?](#como-rodar-pela-primeira-vez-essa-aplicação-)
- [Como transformar o agente em um .exe ?](#como-transformar-o-agente-em-um-.exe-)


## Como rodar o agente pela primeira vez ?

Siga os passos abaixo para rodar a aplicação pela primeira vez:

1. **Clone o projeto**

    Primeiro, você precisa clonar o repositório do projeto. Execute o seguinte comando no seu terminal:

```
git clone https://github.com/seu-usuario/seu-projeto.git
```

2. **Crie um ambiente virtual**Navegue até a pasta do projeto e crie um ambiente virtual. Execute os seguintes comandos:

```
cd Agent
python -m venv venv
```

3. **Ative o ambiente virtual**

   Entre no ambiente virtual com o comando apropriado para o seu sistema operacional:

   - **Windows:**

     ```
     venv\Scripts\activate
     ```
   - **macOS e Linux:**

     ```
     source venv\bin\activate
     ```

**4. Instale as dependências**

    Com o ambiente virtual ativado, instale as bibliotecas necessárias que estão listadas no arquivo`requirements.txt`:

```
pip install -r requirements.txt
```

Este arquivo contém todas as bibliotecas necessárias para o projeto rodar corretamente.

**5. Execute a aplicação**

    Após todas as bibliotecas serem instaladas, você pode iniciar a aplicação com o seguinte comando:

```
python -m app
```

    Esse comando vai iniciar o projeto.




## Como transformar o agente em um .exe ?

Este é o guia para transformar o agente em um arquivo executável (.exe).

##### Pré-requisitos

Certifique-se de que você já criou o ambiente virtual e instalou as bibliotecas que estão no `requirements.txt`.

##### Passos para criar o executável

1. **Entre na pasta `build_tools`**

   Precisamos entrar na pasta `build_tools`, onde está o arquivo de configuração do .exe. Para isso, execute o seguinte comando (é importante estar no ambiente virtual, pois é nele que estão instaladas as bibliotecas necessárias):

   ```
   cd build_tools
   ```
2. **Crie o executável**

   Agora podemos criar nosso executável. Para isso, execute o seguinte comando:

   ```
   pyinstaller app_exe.spec
   ```
3. **Verifique as pastas geradas**

   Após a conclusão do processo, você verá duas novas pastas dentro da pasta `build_tools`, chamadas `build` e `dist`. Nosso executável estará dentro da pasta `dist`.
4. **Adicione os arquivos de configuração**

   Para que o executável funcione corretamente, é necessário colocar os arquivos `configuration.json`, `JobsConfig.json` e `.env` na mesma pasta onde está o executável.

   **Nota:** É crucial que esses arquivos estejam na mesma pasta que o executável, caso não estejam ele não conseguirar achar os mesmo.
5. **Execute o arquivo**

   Após seguir os passos acima, você já pode executar o `arquivo.exe`.
