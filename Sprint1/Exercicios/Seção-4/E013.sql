SELECT 
	cdpro,
	nmcanalvendas,
	nmpro,
	sum(qtd) as quantidade_vendas
from tbvendas 
where status = 'Concluído'
group by cdpro, nmcanalvendas 
order by quantidade_vendas
limit 10