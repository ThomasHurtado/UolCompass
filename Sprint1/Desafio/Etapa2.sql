CREATE VIEW vw_FatoLocacao AS
SELECT 
    L.idLocacao,
    L.idCliente,
    L.idVendedor,
    L.idCarro,
    C.idCombustivel,
    L.dataLocacao,
    L.horaLocacao,
    L.qtdDiaria,
    L.vlrDiaria,
    L.dataEntrega,
    L.horaEntrega
FROM Locacao L
JOIN Carro C ON L.idCarro = C.idCarro

CREATE VIEW vw_DimCliente AS
SELECT 
    idCliente,
    nomeCliente,
    cidadeCliente,
    estadoCliente,
    paisCliente
FROM Cliente

CREATE VIEW vw_DimVendedor AS
SELECT 
    idVendedor,
    nomeVendedor,
    sexoVendedor,
    estadoVendedor
FROM Vendedor

CREATE VIEW vw_DimCarro AS
SELECT 
    idCarro,
    kmCarro,
    classiCarro,
    marcaCarro,
    modeloCarro,
    anoCarro,
    idCombustivel
FROM Carro

CREATE VIEW vw_DimCombustivel AS
SELECT 
    idCombustivel,
    tipoCombustivel
FROM Combustivel