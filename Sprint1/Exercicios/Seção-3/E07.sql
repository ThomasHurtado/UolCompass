select
	au.nome
from autor as au
left join livro as li
	on au.codautor = li.autor
where li.titulo is null
order by au.nome 