from currency_converter import Currency_Converter


ACCESS_KEY = "ddf0f25c0a8193f5b67ff74a907190bb"
url =("http://data.fixer.io/api/latest?access_key="  + ACCESS_KEY)

#Cоздание экземпляра класса
converter = Currency_Converter(url)


#Получение данных от пользователя
from_countty = "RUB"
to_country = "USD"
amount = 100

converter.convert(from_countty, to_country, amount)

#Получение данных от пользователя
from_countty = "USD"
to_country = "RUB"
amount = 100

converter.convert(from_countty, to_country, amount)


#Получение данных от пользователя
from_countty = "EUR"
to_country = "USD"
amount = 100

converter.convert(from_countty, to_country, amount)