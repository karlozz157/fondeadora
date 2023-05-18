from app.apis import TransactionApi
from app.repositories import Repository


class ReconciliationService:
    def __init__(self, api: TransactionApi, repository: Repository):
        self.api = api
        self.repository = repository

    def process(self, date: str) -> dict:
        report = self.__create_report(date)

        if len(report['to_delete']) > 0:
            self.repository.delete_transactions(report['to_delete'])

        if len(report['to_insert']) > 0:
            self.repository.insert_transactions(report['to_insert'])

        if len(report['to_update']) > 0:
            self.repository.update_transactions(report['to_update'])

        return report

    def __create_report(self, date: str) -> dict:
        api_transactions = self.api.get_transactions_by_date(date)
        storage_transactions = self.repository.get_transactions()

        report = {
            'to_delete': [],
            'to_insert': [],
            'to_update': [],
            'transactions': api_transactions,
        }

        api_transaction_ids = []

        for api_transaction in api_transactions:
            transaction_id = api_transaction['transaction_id']

            api_transaction_ids.append(transaction_id)
            storage_transaction = storage_transactions.get(transaction_id)

            if not storage_transaction:
                report['to_insert'].append(self.__get_transaction_to_insert(api_transaction))
                continue

            if api_transaction['amount'] != storage_transaction['amount']:
                report['to_update'].append((transaction_id, api_transaction['amount']))

        storage_transaction_ids = set(storage_transactions.keys())
        report['to_delete'] = list(storage_transaction_ids.difference(set(api_transaction_ids)))

        return report

    def __get_transaction_to_insert(self, transaction: dict) -> tuple:
        return (
            transaction['transaction_id'],
            transaction['user_id'],
            transaction['transaction_type'],
            transaction['amount'],
            transaction['description'],
            transaction['datetime']
        )
