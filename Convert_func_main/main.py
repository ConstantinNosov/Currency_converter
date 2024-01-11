# В основном скрипте

import requests
from currency_converter import convert

ACCESS_KEY = "ddf0f25c0a8193f5b67ff74a907190bb"
url = "http://data.fixer.io/api/latest?access_key=" + ACCESS_KEY
data = requests.get(url).json()
rates = data["rates"]

# Получение данных от пользователя
from_country = input("Введи валюту для конвертации:")
to_country = input("Во что конвертируем:")
amount = int(input("Введи сумму:"))

# Вызов функции
convert(from_country, to_country, amount, rates)