



# API Centralizadora de Agentes

## Índice

1. [Introdução](#introdução)
2. [Para que server o Centralizador dos agentes ?](O-que-é-o-Centralizador-dos-agentes-?)
3. [Como rodar a api pela primeira vez ?]()
4. [Como o centralizador funciona por baixo dos panos ?]()
5. [Quais possíveis erros e como resolver ?]()
6. [Como Transformar a API em um Executável (.exe)](#como-transformar-a-api-em-um-executável-exe)
6. [Como publicar o centralizador no IIS]()
7. [Como publicar o centralizador no CMD(Escondido)]()
8. [Como publicar o centralizador em um serviço do windows?]()
9. [Conclusão](#conclusão) 

## Introdução

Esta documentação fornece informações de extrema importancia para o desenvolvedor, no decorrer da documentação você irá entender o que é essa api, qual a importacia e objetivo dela, como rodar ela em ambiente de teste,ferramentas necessarias para trabalhar junto com essa aplicação e será disponibilizado uma documentação detalhada dos endpoints... 


## Para que Serve o Centralizador dos Agentes?


<p align="left">
Você já se perguntou por que precisamos de um centralizador para os agentes? Imagine a seguinte situação: você tem que acessar cada um dos seus agentes individualmente para alterar uma configuração, verificar se o agente está ativo ou monitorar o status do servidor. Se você tiver apenas um agente, essa tarefa é relativamente simples. No entanto, monitorar e gerenciar 15 ou 20 agentes individualmente se torna uma tarefa extremamente trabalhosa.
<p/>

### Propósito

O centralizador de agentes foi criado exatamente para resolver esse problema. Ele permite que você centralize e gerencie todas as informações dos seus agentes em um único lugar. Com isso, você pode:
<p align="center">

- **Monitorar a Atividade dos Agentes**: Verificar se cada agente está ativo e funcionando corretamente.
- **Gerenciar Configurações**: Alterar configurações de todos os agentes de forma centralizada, sem a necessidade de acessá-los individualmente.
- **Verificar Status dos Servidores**: Monitorar o status dos servidores associados aos agentes.
<p/>

### Funcionamento
<p align="center">

Atualmente, a comunicação entre o centralizador e os agentes é feita por meio de mensageria utilizando o RabbitMQ. Isso permite que os agentes informem ao centralizador sobre os jobs que estão rodando e troquem informações sobre o status dos servidores.

Além disso, o centralizador utiliza o protocolo WebSocket para verificar se os servidores estão ativos, proporcionando uma comunicação em tempo real e eficiente.
<p/>

### Benefícios
<p align="left">

- **Centralização**: Facilita a gestão e monitoramento de múltiplos agentes a partir de uma interface única.
- **Eficiência**: Reduz o tempo e esforço necessário para gerenciar grandes quantidades de agentes.
- **Escalabilidade**: Suporta o crescimento da infraestrutura, permitindo a adição de novos agentes sem complicações.
<p/>


<p align="center">
O centralizador de agentes é uma ferramenta essencial para qualquer ambiente que utilize múltiplos agentes. Ele simplifica a administração e melhora a eficiência operacional, garantindo que você tenha todas as informações necessárias ao seu alcance.
<p/>


## Como rodar a api pela primeira vez ?

Siga os passos abaixo para rodar a aplicação pela primeira vez:

### 1. Clone o Projeto

Primeiro, você precisa clonar o repositório do projeto. Execute o seguinte comando no seu terminal:

```bash
git clone https://github.com/seu-usuario/sua-api.git
```

### 2. Crie um Ambiente Virtual

Navegue até a pasta do projeto e crie um ambiente virtual. Execute os seguintes comandos:

```bash
cd sua-api
python -m venv venv
```

### 3. Ative o Ambiente Virtual

Entre no ambiente virtual com o comando apropriado para o seu sistema operacional:

- **Windows:**

    ```bash
    venv\Scripts\activate
    ```

- **macOS e Linux:**

    ```bash
    source venv/bin/activate
    ```

### 4. Instale as Dependências

Com o ambiente virtual ativado, instale as bibliotecas necessárias que estão listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 5. Execute a Aplicação

Após todas as bibliotecas serem instaladas, você pode iniciar a aplicação com o seguinte comando(lembrando que tem que ser no ambiente virtual que criamos):

```bash
python -m app
```

Esse comando vai iniciar o projeto.



    

## Como o centralizador funciona por baixo dos panos ?

 - Entender o funcionamento interno do centralizador é crucial para quem pretende trabalhar com este projeto. Assim como conhecer uma empresa antes de começar a trabalhar nela, é importante conhecer o código e as ferramentas utilizadas no projeto. Esta seção fornece uma visão geral das tecnologias e mecanismos que sustentam o centralizador de agentes.

**O centralizador de agentes utiliza um sistema de mensageria, especificamente o RabbitMQ, para facilitar a comunicação entre o centralizador e os agentes. Esta arquitetura permite que as mensagens sejam trocadas de forma eficiente e em tempo real, garantindo a sincronização e a atualização dos dados entre os componentes.**


Para trocar informações sobre o status do servidor ou informações em tempo real do servidor (CPU, RAM, DISCO, etc.), é usado WebSocket, pois ele garante comunicação constante e imediata. Diferente do RabbitMQ, onde pode acontecer do centralizador enviar uma alteração para o agente, mas o mesmo estar offline no momento,porém quando agente voltar a ficar online ele vai pegar essa mensagem,o WebSocket assegura que a comunicação seja mantida continuamente, garantido que o responsável pelo servidor saiba que esse servidor ficou OFFLINE




## Quais possíveis erros e como resolver ?

**Enviei uma mensagem do centralizador, porem o agente não recebeu ou virse-versa:** Um dos pontos que deve ser verificado é se o seu rabbit está rodando - Caso esteja tudo OK com ele, verifique se o .env está apontando para o servidor do rabbit corretamente e se o usuario e senha dele está correto




## Como Transformar a API em um Executável (.exe)

Este é o guia para transformar a API em um arquivo executável (.exe).

### Pré-requisitos

Certifique-se de que você já criou o ambiente virtual e instalou as bibliotecas que estão no `requirements.txt`.

### Passos para Criar o Executável

1. **Entre na Pasta build_tools**

    Precisamos entrar na pasta `build_tools`, onde está o arquivo de configuração do .exe. Para isso, execute o seguinte comando (é importante estar no ambiente virtual, pois é nele que estão instaladas as bibliotecas necessárias):

    ```bash
    cd build_tools
    ```

2. **Crie o Executável**

    Agora podemos criar nosso executável. Para isso, execute o seguinte comando:

    ```bash
    pyinstaller app_exe.spec
    ```

3. **Verifique as Pastas Geradas**

    Após a conclusão do processo, você verá duas novas pastas dentro da pasta `build_tools`, chamadas `build` e `dist`. Nosso executável estará dentro da pasta `dist`.

4. **Adicione os Arquivos de Configuração**

    Para que o executável funcione corretamente, é necessário colocar o arquivo `.env` na mesma pasta onde está o executável.

    **Nota:** É crucial que esses arquivos estejam na mesma pasta que o executável, caso contrário ele não conseguirá encontrar os mesmos.

5. **Execute o Arquivo**

    Após seguir os passos acima, você já pode executar o arquivo `.exe`.
    

## Como publicar no IIS?
 **EM ANDAMENTO**

## Como publicar no CMD(Escondido)?
 **EM ANDAMENTO**
 
## Como publicar em um serviço do windows
 **EM ANDAMENTO**

    


## Conclusão

Esta documentação abrange os principais aspectos da configuração, execução e transformação da API em um executável. Para mais informações ou dúvidas, consulte a documentação oficial ou entre em contato com o suporte.

