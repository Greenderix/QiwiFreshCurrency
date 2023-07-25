import argparse
import api_cbr

parser = argparse.ArgumentParser(description="Утилита для получения курса валюты.")
parser.add_argument("--code", type=str, help="Код валюты (например, USD, EUR, etc.)", required=True)
parser.add_argument("--date", type=str, help="Дата в формате ГГГГ-ММ-ДД", required=True)

args = parser.parse_args()

value, name = api_cbr.get_currency_rate(args.code, args.date)
print(f"{args.code} ({name}): {value}")
