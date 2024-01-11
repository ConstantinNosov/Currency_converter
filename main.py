from currency_converter import Currency_Converter


ACCESS_KEY = "ddf0f25c0a8193f5b67ff74a907190bb"
url =("http://data.fixer.io/api/latest?access_key="  + ACCESS_KEY)

#Cоздание экземпляра класса
converter = Currency_Converter(url)


#Получение данных от пользователя
from_countty = input("Введи валюту для конвертации:")
to_country = (input("Во что конвертируем:"))
amount = int(input("Введи сумму:"))

converter.convert(from_countty, to_country, amount)