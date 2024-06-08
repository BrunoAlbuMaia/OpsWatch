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
usuarioCriacao VARCHAR(20),
usuarioAlteracao VARCHAR(20),
FOREIGN KEY (nrServidorId) REFERENCES Servidores(nrServidorId)
)



---Description dos PLUGINS ---
CREATE TABLE Descriptions(
nrDescriptionId INT IDENTITY(1,1) PRIMARY KEY,
nmChavePlugin VARCHAR(30) NOT NULL,
nmJsonPlugin VARCHAR(800) NOT NULL,
descricao VARCHAR(500) NOT NULL
);



CREATE TRIGGER after_insert_servidores
ON Servidores
AFTER INSERT
AS
BEGIN
    INSERT INTO Jobs (nrServidorId, dtCriacao, usuarioCriacao)
    SELECT 
        inserted.nrServidorId, 
        GETDATE(), 
        'dbIntegrador'
    FROM inserted;
END;

