FROM python:3

RUN pip install pandas

WORKDIR /etl

COPY . .

CMD ["python", "./etl.py"]

