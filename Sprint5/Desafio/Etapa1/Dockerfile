FROM python:3

RUN pip install boto3 logging 

WORKDIR /etapa-1

COPY . .

RUN mkdir /data

CMD ["python", "./etapa-1.py"]