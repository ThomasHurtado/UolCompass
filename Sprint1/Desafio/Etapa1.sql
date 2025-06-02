CREATE TABLE Cliente(
	idCliente int PRIMARY KEY,
	nomeCliente varchar,
	cidadeCliente varchar,
	estadoCliente varchar,
	paisCliente varchar,
)

CREATE TABLE Vendedor(
	idVendedor int PRIMARY KEY,
	nomeVendedor varchar,
	sexoVendedor varchar,
	estadoVendedor varchar
)

CREATE TABLE Combustivel (
    idCombustivel INT PRIMARY KEY,
    tipoCombustivel VARCHAR
)

CREATE TABLE Carro (
    idCarro INT PRIMARY KEY,
    kmCarro INT,
    classiCarro VARCHAR,
    marcaCarro VARCHAR,
    modeloCarro VARCHAR,
    anoCarro INT,
    idCombustivel INT,
    FOREIGN KEY (idCombustivel) REFERENCES Combustivel(idCombustivel)
)

CREATE TABLE Locacao (
    idLocacao INT PRIMARY KEY,
    idCliente INT,
    idCarro INT,
    idVendedor INT,
    dataLocacao DATE,
    horaLocacao TIME,
    qtdDiaria INT,
    vlrDiaria DECIMAL(10,2),
    dataEntrega DATE,
    horaEntrega TIME,
    FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente),
    FOREIGN KEY (idCarro) REFERENCES Carro(idCarro),
    FOREIGN KEY (idVendedor) REFERENCES Vendedor(idVendedor)
)