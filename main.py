from fastapi import FastAPI
from app.apis import TransactionApi
from app.readers import TransactionCsvReader
from app.repositories import TransactionSqliteRepository
from app.seeders import TransactionSeeder
from app.services import ReconciliationService
from app.utils import get_http_exception


app = FastAPI()


@app.get("/")
def who_am_i():
    return {"who_am_i": "carlin"}


@app.post("/seed")
def seed() -> dict:
    try:
        seeder = TransactionSeeder(TransactionCsvReader(), TransactionSqliteRepository())
        seeder.seed()
    except Exception as e:
        raise get_http_exception(e)
    return {"data": "seed executed successful"}


@app.get("/transactions/{user_id}")
def get_transactions_by_user_id(user_id: int) -> dict:
    try:
        repository = TransactionSqliteRepository()
        transactions = repository.get_transactions_by_user_id(user_id)
    except Exception as e:
        raise get_http_exception(e)
    return {"data": transactions}


@app.post("/report")
def create_report(date: str) -> dict:
    try:
        service = ReconciliationService(TransactionApi(), TransactionSqliteRepository())
        report = service.process(date)
    except Exception as e:
        raise get_http_exception(e)
    return {"data": report}


@app.get("/report/{date}")
def get_report(date: str) -> dict:
    try:
        repository = TransactionSqliteRepository()
        transactions = repository.get_transactions_by_date(date)
    except Exception as e:
        raise get_http_exception(e)
    return {"data": transactions}
