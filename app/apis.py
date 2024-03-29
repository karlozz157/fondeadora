import requests
import os
from datetime import datetime
from app.utils import check_valid_date, FORMAT_DATE
from app.exceptions import ResponseInvalidError, DateInvalidRangeError


class TransactionApi:
    def __init__(self):
        self.api_url = os.getenv('TRANSACTIONS_ENDPOINT')

    def get_transactions_by_date(self, date: str) -> list:
        date_as_object = check_valid_date(date)
        self.check_valid_date_range(date_as_object)

        response = requests.post(self.api_url, json={'date': date})

        if response.status_code != requests.status_codes.codes.OK:
            raise ResponseInvalidError(response.text)

        return response.json()

    def check_valid_date_range(self, date) -> None:
        api_allow_date_min = os.getenv("API_ALLOW_DATE_MIN")
        api_allow_date_max = os.getenv("API_ALLOW_DATE_MAX")

        min_date = datetime.strptime(api_allow_date_min, FORMAT_DATE).date()
        max_date = datetime.strptime(api_allow_date_max, FORMAT_DATE).date()

        if not (min_date <= date <= max_date):
            raise DateInvalidRangeError(api_allow_date_min, api_allow_date_max)
