from app.repositories import Repository
from app.readers import Reader


class TransactionSeeder:
    def __init__(self, reader: Reader, repository: Repository) -> None:
        self.reader = reader
        self.repository = repository

    def seed(self) -> None:
        transactions = self.reader.get_transactions()
        self.repository.migrate()
        self.repository.insert_transactions(transactions)
