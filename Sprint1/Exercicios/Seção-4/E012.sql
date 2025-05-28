with somar_vendas as(
	SELECT
    	cdvdd,
    	SUM(qtd * vrunt) AS valor_venda
	FROM tbvendas
	WHERE status = 'Concluído'
	GROUP BY cdvdd
	order by valor_venda asc
	limit 1
)
select
	dp.cddep,
	dp.nmdep,
	dp.dtnasc,
	valor_venda as valor_total_vendas
from somar_vendas as soma
left join tbdependente as dp
	on soma.cdvdd = dp.cdvdd
left join tbvendedor as vend
	on soma.cdvdd = vend.cdvdd