with somar_vendas as(
	SELECT
    	cdvdd,
    	SUM(qtd * vrunt) AS valor_venda
	FROM tbvendas
	WHERE status = 'Concluído'
	GROUP BY cdvdd
)
select
	vendedor.nmvdd as 'vendedor',
	soma.valor_venda as valor_total_vendas,
	ROUND(soma.valor_venda * (vendedor.perccomissao / 100.0), 2) as comissao
from tbvendedor as vendedor
left join somar_vendas as soma
	on vendedor.cdvdd = soma.cdvdd
order by comissao desc