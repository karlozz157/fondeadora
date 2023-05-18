from app.apis import TransactionApi
from app.repositories import Repository
from app.services import ReconciliationService
from unittest.mock import Mock


class TestReconciliationService:

    def test_process(self):
        self.__initialize()
        report = self.reconciliation_service.process('2023-05-18')

        assert report['to_delete'] == [2]
        assert report['to_update'] == [(1, 100)]

        api_transactions = self.__get_api_transactions()
        transaction_to_insert = api_transactions[1]
        assert report['to_insert'] == [tuple(transaction_to_insert.values())]

    def __get_db_transactions(self) -> dict:
        return {
            1: {
                "transaction_id": 1,
                "user_id": 1002,
                "transaction_type": "debit",
                "amount": 1025,
                "description": "Está transacción será actualziada",
                "datetime": "2023-03-06T18:48:29"
            },
            2: {
                "transaction_id": 2,
                "user_id": 1002,
                "transaction_type": "debit",
                "amount": 1025,
                "description": "Está transacción será eliminada",
                "datetime": "2023-03-06T18:48:29"
            }
        }

    def __get_api_transactions(self) -> list:
        return [
            {
                "transaction_id": 1,
                "user_id": 1002,
                "transaction_type": "debit",
                "amount": 100,
                "description": "Está transacción será actualziada",
                "datetime": "2023-03-06T18:48:29"
            },
            {
                "transaction_id": 3,
                "user_id": 1002,
                "transaction_type": "debit",
                "amount": 300,
                "description": "Está transacción será insertada",
                "datetime": "2023-03-06T18:48:29"
            },
        ]

    def __initialize(self) -> None:
        repository_mock = Mock(spec=Repository)
        repository_mock.get_transactions.return_value = self.__get_db_transactions()
        api_service_mock = Mock(spec=TransactionApi)
        api_service_mock.get_transactions_by_date.return_value = self.__get_api_transactions()
        self.reconciliation_service = ReconciliationService(api_service_mock, repository_mock)
