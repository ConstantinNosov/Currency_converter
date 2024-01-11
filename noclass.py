import requests


ACCESS_KEY = "ddf0f25c0a8193f5b67ff74a907190bb"
url =("http://data.fixer.io/api/latest?access_key="  + ACCESS_KEY)
data = requests.get(url).json()
rates = data["rates"]
#print(data)
#print(rates)

#Получение данных от пользователя
from_countty = input("Введи валюту для конвертации:")
to_country = (input("Во что конвертируем:"))
amount = int(input("Введи сумму:"))

def convert(from_currency, to_currency, amount):
    initial_amount = amount
    #т.к. базовой валютой является евро,то выполняем
    if from_currency != 'EUR':
        amount = amount / rates[from_currency]
    output = amount * rates[to_currency]
    #Округление преобразования  до двух знаков после запятой
    output = round(amount * rates[to_currency], 2)
    #Вывод в красивом формате для печати
    print('{} {}  = {} {}'.format(initial_amount, from_currency, output, to_currency))
    
#Вызов функции
convert(from_countty, to_country, amount)

