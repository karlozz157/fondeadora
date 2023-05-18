import abc
import csv
import os


class Reader(metaclass=abc.ABCMeta):
    _data = {}

    @abc.abstractmethod
    def get_transactions(self) -> list:
        pass


class TransactionCsvReader(Reader):
    def get_transactions(self) -> list:
        transactions_csv_file = os.getenv('TRANSACTIONS_CSV_FILE')
        with open(transactions_csv_file, newline='') as csvfile:
            reader = csv.reader(csvfile)
            rows = [row for key, row in enumerate(reader) if key != 0]
        return rows
