# Desafio da Sprint

O desafio da Sprint consiste em realizar a normalização de uma base de dados, sendo necessario aplicar as formas normais para transforma-lá em 
um modelo relacional e posteriormente em um modelo dimensional.

A realização deste desafio estará divido em 2 etapas

## Etapa 1

O objetivo desta etapa é tranformar a base de dados em um modelo relacional, aplicando as formas normais.
Para isso foi seguido as seguintes etapas:

- Utilização do Dbeaver para modifcar a base de dados
[DBeaver](./Evidencias/1-DBeaver.png)

- Aplicar a Primera Forma Normal (1FN), porém a base de dados ja esta nessa forma, não há campos multivalorados
- Aplicar a Segunda Forma Normal (2FN), com isso separei em objetos diferentes, criando tabelas distintas. Foram criadas as tabelas Carro, Locação, Combustivel, Cliente e Vendedor

[CriacaoTabelas](./Evidencias/2-Criação_Tabelas.png)

- Aplicar a Terceira Forma Normal (3FN), porém as tabelas ja estão nesse formato
- Construir a visualizacao do modelo Relacional

[ModeloRelacional](./Evidencias/3-Modelo-Relacional.png)
