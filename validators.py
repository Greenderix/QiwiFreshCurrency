from datetime import datetime

from exceptions import IncorrectDateError


def is_valid_date(date_str):
    try:
        input_date = datetime.strptime(date_str, '%Y-%m-%d')
        today = datetime.now().date()

        if input_date.date() <= today:
            formatted_date = input_date.strftime('%d/%m/%Y')
            return formatted_date
        else:
            return None

    except ValueError:
        raise IncorrectDateError("Incorrect date")
