SELECT
    au.nome,
    au.codautor,
    au.nascimento,
    COUNT(li.cod) AS quantidade
FROM autor AS au
LEFT JOIN livro AS li
    ON au.codautor = li.autor
GROUP BY au.codautor, au.nome, au.nascimento
ORDER BY REPLACE(au.nome, 'Á', 'A') ASC