select distinct
	au.nome
from livro as li
join editora  as edi
	on li.editora = edi.codeditora
join autor as au
	on li.autor = au.codautor
join endereco as ende
	on edi.endereco = ende.codendereco
where ende.estado not in ('RIO GRANDE DO SUL', 'PARANÁ')
order by au.nome