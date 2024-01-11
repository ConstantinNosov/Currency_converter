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
