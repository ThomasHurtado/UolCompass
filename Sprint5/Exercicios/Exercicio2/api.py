import requests
import pandas as pd
from IPython.display import display
import os
from dotenv import load_dotenv

load_dotenv('.env')

api_key = os.getenv('key_api')

url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&amp;language=pt-BR"

response = requests.get(url)

data = response.json()

filmes = []

for movie in data['results']:
    df = {'Titulo' : movie['title'],
          'Lançamento': movie['release_date'],
          'Visão geral': movie['overview'],
          'Votos': movie['vote_count'],
          'Media de votos': movie['vote_average']}
    filmes.append(df)

df = pd.DataFrame(filmes)

display(df)

print(response.text)