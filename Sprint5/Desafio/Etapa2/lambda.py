import requests
import boto3
import json
import os
from datetime import date

def lambda_handler(event, context):
    hoje = date.today()

    api = os.environ['IMDB_API_KEY']

    url = 'https://api.themoviedb.org/3/discover/tv'

    params = {
    'api_key': api,
    'language': 'pt-BR',
    'sort_by': 'vote_average.desc',   
    'with_genres': '16',              
    'with_origin_country': 'JP',      
    'vote_count.gte': 100,            
    'page': 1
    }

    response = requests.get(url, params=params)

    data = response.json()
    json_file = json.dumps(data, indent=2, ensure_ascii=False)

    s3 = boto3.client('s3')

    bucket_name = 'desafio-final-thomas'

    s3.put_object(
    Bucket= bucket_name,
    Key=f"Raw/TMDB/JSON/{hoje.year}/{hoje.month}/{hoje.day}/animes.json",
    Body=json_file,
    ContentType='application/json'
    )

    limite = 10
    contador = 0

    for anime in data['results']:

        url = f"https://api.themoviedb.org/3/tv/{anime['id']}"

        params = {
            'api_key': api,
            'language': 'pt-BR',
        }

        response = requests.get(url, params=params)
        data = response.json()
        json_file = json.dumps(data, indent=2, ensure_ascii=False)

        s3.put_object(
        Bucket= bucket_name,
        Key=f"Raw/TMDB/JSON/{hoje.year}/{hoje.month}/{hoje.day}/{anime['id']}.json",
        Body=json_file,
        ContentType='application/json'
        )

        contador += 1
        if contador == limite:
            break
    


