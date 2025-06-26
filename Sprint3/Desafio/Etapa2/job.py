import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    db = pd.read_csv('/dados/csv_limpo.csv')

    with open('/dados/resposta.txt', 'w'):
        pass

    ## Q1
    filter1 = db.groupby('Artist').agg(contagem=('Artist', 'count'), total_gross=('Actual gross', 'sum')).sort_values(['contagem', 'total_gross'], ascending=False).max()
    with open('/dados/resposta.txt', 'a') as e:
        e.write(f'Resposta Exercicio 1:\n\n \
    O artista que mais apareceu teve {filter1['contagem']} aparições.\n \
    O maior valor bruto arrecadado por um artista foi de ${filter1['total_gross']}')
        e.close()

    ##Q2
    filter2 = db[['Tour title', 'Average gross']].loc[db['Start year'] == db['End year']].max()
    with open('/dados/resposta.txt', 'a') as e:
        e.write(f'\n\nResposta Exercicio 2:\n\n \
    A turne com o maior faturamento dentro de um ano foi a {filter2['Tour title']} com ${filter2['Average gross']}')

    ##Q3
    db['Actual AVG'] = db['Adjustedgross (in 2022 dollars)'].astype(int) / db['Shows'].astype(int)
    db['Actual AVG'] = db['Actual AVG'].astype(float).round(2)
    filter3 = db[['Artist', 'Tour title', 'Actual AVG']].sort_values('Actual AVG', ascending=False).head(3).reset_index().to_dict(orient='records')
    with open('/dados/resposta.txt', 'a') as e:
        e.write(f'\n\nResposta Exercicio 3:\n\n')
        for linha in filter3:
            e.write(f' - {linha['Artist']} em {linha['Tour title']} com o valor de ${linha['Actual AVG']}\n')
    e.close()

    ##Q4
    popular = db.groupby('Artist').agg(contagem=('Artist', 'count'), total_gross=('Actual gross', 'sum')).sort_values(['contagem', 'total_gross'], ascending=False)
    name = popular.index[0]

    filter4 = db[['Actual gross', 'Start year']].loc[db['Artist'] == name]

    plt.plot(filter4['Start year'], filter4['Actual gross'], marker='o')
    plt.title('Arrecadação por cada ano de turne')
    plt.ylabel('Arrecadação (por 100 milhões de $)')
    plt.xlabel('Ano da turne')
    plt.savefig('/dados/q4.png')
    plt.close()

    ##Q5
    filter = db[['Artist', 'Shows']].groupby('Artist').agg(total_shows=('Shows', 'sum')).sort_values(['total_shows'], ascending=False).head()

    plt.bar(filter.index, filter['total_shows'])
    plt.title('Numero de shows por artista')
    plt.ylabel('Numero de shows')
    plt.xlabel('Artista')
    plt.savefig('/dados/q5.png')
    plt.close()

    
