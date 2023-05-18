FROM python:3.9-slim

ENV API_ALLOW_DATE_MIN="2023-03-01"
ENV API_ALLOW_DATE_MAX="2023-03-07"
ENV DATABASE_NAME="./fondeadora.db"
ENV TRANSACTIONS_CSV_FILE="./transactions.csv"
ENV TRANSACTIONS_ENDPOINT="https://eoylo519qvrfijk.m.pipedream.net"

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
