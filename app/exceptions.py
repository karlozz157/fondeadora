from fastapi import status


class DateInvalidError(Exception):
    ERROR = 'Fecha no válida. El formato correcto es el siguiente: 2023-03-16'

    def __init__(self):
        self.status_code = status.HTTP_400_BAD_REQUEST
        super().__init__(self.ERROR)


class DateInvalidRangeError(Exception):
    ERROR = 'El rango de la fecha debe ser entre %s y %s'

    def __init__(self, min_date: str, max_date: str):
        self.status_code = status.HTTP_400_BAD_REQUEST
        super().__init__(self.ERROR % (min_date, max_date))


class ResponseInvalidError(Exception):
    ERROR = 'El response no fue exitoso: Error: %s'

    def __init__(self, message: str):
        self.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        super().__init__(self.ERROR % message)
