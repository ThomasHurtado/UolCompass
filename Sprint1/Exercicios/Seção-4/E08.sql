SELECT
	venda.cdvdd,
	vendedor.nmvdd
from tbvendedor as vendedor
left join tbvendas as venda
	on vendedor.cdvdd = venda.cdvdd
group by venda.cdvdd
order by count(venda.cdvdd) desc
limit 1

