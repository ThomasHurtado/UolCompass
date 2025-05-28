SELECT 
	au.codautor,
	au.nome,
	count(*) as quantidade_publicacoes
from autor as au
left join livro as li
	on au.codautor = li.autor
group by au.codautor
order by quantidade_publicacoes desc
limit 1


