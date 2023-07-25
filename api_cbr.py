import requests
import xml.etree.ElementTree as ET

import validators
from exceptions import IncorrectCodeError


def find_value_by_charcode(xml_data, charcode):
    root = ET.fromstring(xml_data)
    for valute in root.findall('.//Valute'):
        if valute.find('CharCode').text == charcode:
            value = valute.find('Value').text
            name = valute.find('Name').text
            return [value, name]
    raise IncorrectCodeError("Incorrect code")


def get_currency_rate(code, date):
    date = validators.is_valid_date(date)
    url = f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={date}'
    xml_response = requests.get(url).content
    return find_value_by_charcode(xml_response, code)
