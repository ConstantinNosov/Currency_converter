import requests

#создание класса конверора  валют
class Currency_Converter:
    #Словарь для хранения курсов валют
    #rates - это статическое поле класса, представляющее словарь для хранения курсов валют.
    rates = {}

    #Принимает параметр url - адрес для запроса данных о курсах валют.
    def __init__(self, url):
        #Запрос данных с url
        data = requests.get(url).json()
        #Извлечение курсов валют из плученых данных
        self.rates = data["rates"]

    #Функция выполнения конвертации 
    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        #т.к. базовой валютой является евро,то выполняем
        if from_currency != 'EUR':
            amount = amount / self.rates[from_currency]
        output = amount * self.rates[to_currency]
        #Округление преобразования  до двух знаков после запятой
        output = round(amount * self.rates[to_currency], 2)
        #Вывод в красивом формате для печати
        print('{} {}  = {} {}'.format(initial_amount, from_currency, output, to_currency))

#Точка входа в приложение 
if __name__ == "__main__":

    ACCESS_KEY = "ddf0f25c0a8193f5b67ff74a907190bb"
    url =("http://data.fixer.io/api/latest?access_key="  + ACCESS_KEY)

    #Cоздание экземпляра класса
    converter = Currency_Converter(url)


    #Получение данных от пользователя
    from_countty = input("Введи валюту для конвертации:")
    to_country = (input("Во что конвертируем:"))
    amount = int(input("Введи сумму:"))

    #
    converter.convert(from_countty, to_country, amount)