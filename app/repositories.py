import abc
import sqlite3
import os
from app.utils import check_valid_date


class Repository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def delete_transactions(self, transaction_ids: []):
        pass

    @abc.abstractmethod
    def get_transactions(self) -> dict:
        pass

    @abc.abstractmethod
    def get_transactions_by_date(self, date: str) -> dict:
        pass

    @abc.abstractmethod
    def insert_transactions(self, transactions: list) -> list:
        pass

    @abc.abstractmethod
    def migrate(self) -> None:
        pass

    @abc.abstractmethod
    def update_transactions(self, transactions: list) -> dict:
        pass


class TransactionSqliteRepository(Repository):
    def __init__(self):
        self.connection = sqlite3.connect(os.getenv("DATABASE_NAME"))
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def delete_transactions(self, transaction_ids: list):
        query = 'DELETE FROM transactions WHERE transaction_id IN ({})'.format(','.join(['?'] * len(transaction_ids)))
        self.cursor.execute(query, transaction_ids)
        self.connection.commit()

    def get_transactions(self) -> dict:
        query = 'SELECT transaction_id, amount FROM transactions'
        self.cursor.execute(query)
        return {row["transaction_id"]: dict(row) for row in self.cursor.fetchall()}

    def get_transactions_by_date(self, date: str) -> list:
        check_valid_date(date)
        query = 'SELECT * FROM transactions WHERE datetime LIKE ?'
        self.cursor.execute(query, (f'{date}%',))
        return self.cursor.fetchall()

    def insert_transactions(self, transactions: list):
        query = """
                INSERT INTO transactions (
                    transaction_id,
                    user_id,
                    transaction_type,
                    amount,
                    description,
                    datetime
                ) VALUES (?,?,?,?,?,?)
                """

        self.cursor.executemany(query, transactions)
        self.connection.commit()

    def migrate(self):
        query = """
                CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    transaction_id INTEGER UNIQUE,
                    user_id INTEGER,
                    transaction_type TEXT,
                    amount REAL,
                    description TEXT,
                    datetime TEXT
                )
                """
        self.cursor.execute(query)
        self.cursor.execute('DELETE FROM transactions')
        self.connection.commit()

    def update_transactions(self, transactions: list):
        query = "UPDATE transactions SET amount = ? WHERE transaction_id = ?"
        self.cursor.executemany(query, transactions)
        self.connection.commit()
