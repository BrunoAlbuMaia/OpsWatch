CREATE DATABASE dbIntegrador
 
CREATE TABLE Servidores (
nrServidorId INT IDENTITY PRIMARY KEY NOT NULL,
nmServidor VARCHAR(25) NOT NULL,
nmIpServidor VARCHAR(20) NOT NULL,
nmDescricao VARCHAR(200) NULL,
urlWebsocketServidor VARCHAR(100) NULL,
urlWebSocketJobs VARCHAR(100) NULL,
flAtivo BIT DEFAULT  1
)

----- JOBS -----
CREATE TABLE Jobs(
nrServidorId  INT NOT NULL,
jsonConfig VARCHAR(MAX),
dtCriacao DATETIME,
dtAtualizacao DATETIME,
usuarioAlteracao VARCHAR(20),
FOREIGN KEY (nrServidorId) REFERENCES Servidores(nrServidorId)
)

CREATE TABLE CssReplicJobs(
nrServidorId  INT NOT NULL,
jsonConfig VARCHAR(MAX),
dtGravada DATETIME
)

