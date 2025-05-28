select
	codeditora as CodEditora,
	nome as NometEditora,
	count(li.cod) as QuantidadeLivros
from livro as li
left join editora as edi
	on li.editora = edi.codeditora
group by codeditora