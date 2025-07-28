import boto3
from botocore.exceptions import ClientError
import logging


if __name__ == "__main__":

    aws_access_key_id = input("Digite a aws access key id: ")
    aws_secret_access_key = input("Digite a aws secret access key: ")
    aws_session_token = input("Digite a aws session token: ")

    s3 = boto3.client('s3',
        aws_access_key_id= aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        aws_session_token=aws_session_token,
        region_name='us-east-1'
    )

    bucket_name = 'desafio-final-thomas'
    file_name = 'movies.csv'
    s3_path = 'Raw/Local/CSV/Movies/2025/07/22/movies.csv'

    try:
        s3.upload_file(file_name, bucket_name, s3_path)
        print(f"Arquivo {file_name} enviado com sucesso")
    except ClientError as e:
        logging.error(e)
    
    file_name = 'series.csv'
    s3_path = 'Raw/Local/CSV/Series/2025/07/22/series.csv'

    try:
        s3.upload_file(file_name, bucket_name, s3_path)
        print(f"Arquivo {file_name} enviado com sucesso")
    except ClientError as e:
        logging.error(e)
    

