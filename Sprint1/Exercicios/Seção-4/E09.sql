SELECT 
    cdpro,
    nmpro
FROM tbvendas
WHERE DATE(dtven) BETWEEN '2014-02-03' AND '2018-02-02'
group by cdpro
order by count(cdpro) desc
limit 1