select
	cod as CodLivro,
	titulo as Titulo,
	autor as CodAutor,
	valor as Valor,
	editora as CodEditora,
	edi.nome as NomeEditora
	from livro as li
	left join editora as edi
		on li.editora = edi.codeditora
	order by valor desc
	limit 10