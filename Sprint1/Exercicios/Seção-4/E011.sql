SELECT
        cdcli,
        nmcli,
        SUM(qtd * vrunt) AS gasto
    FROM tbvendas
    WHERE status = 'Concluído'
    GROUP BY cdcli
    order by gasto desc
    limit 1