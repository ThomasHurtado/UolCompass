SELECT 
    COUNT(li.cod) AS quantidade,
    edi.nome,
    ende.estado,
    ende.cidade
FROM editora AS edi
LEFT JOIN livro AS li
    ON edi.codeditora = li.editora
LEFT JOIN endereco AS ende
    ON edi.endereco = ende.codendereco
GROUP BY edi.nome, ende.estado, ende.cidade
HAVING quantidade > 0
ORDER BY quantidade DESC
LIMIT 5;