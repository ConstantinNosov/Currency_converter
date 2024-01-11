import tkinter as tk
import requests

window = tk.Tk()

window.title("Currency_converter")

#Создание виджетов для текстовых меток 
input_label = tk.Label(window, text = "Введи сумму:", font ="arial 12 bold", borderwidth = 10)
label_fc = tk.Label(window, text="Что конвертруем:",font ="arial 12 bold", borderwidth = 10)
label_tc = tk.Label(window, text="Во что конвертируем:", font ="arial 12 bold", borderwidth = 10)
outputlabel = tk.Label(window, text="Сумма:", font ="arial 12 bold", borderwidth = 10)

#Создание виджетов  для  полей  ввода
input_amount = tk.Entry(window, font = "arial 12 bold", borderwidth=5)
form_currency = tk.Entry(window, font = "arial 12 bold", borderwidth=5)
to_currency = tk.Entry(window, font = "arial 12 bold", borderwidth=5)
output = tk.Entry(window, font = "arial 12 bold", borderwidth=5)

#Размещение виджетов в окне
input_label.grid(row = 0, column = 0)
label_fc.grid(row = 1, column = 0)
label_tc.grid(row = 2, column = 0)
input_amount.grid(row = 0, column = 1)
form_currency.grid(row = 1, column = 1)
to_currency.grid(row = 2, column = 1)
outputlabel.grid(row = 4, column = 0)
output.grid(row = 4, column = 1)


ACCESS_KEY = "ddf0f25c0a8193f5b67ff74a907190bb"
url =("http://data.fixer.io/api/latest?access_key="  + ACCESS_KEY)
#Запрос данных с url
data = requests.get(url).json()
#Извлечение курсов валют из плученых данных
rates = data["rates"]
print(rates)

#Функция преобразования
def currency_converter( from_currency, to_currency, input_amount):
    from_currency = from_currency.get()
    to_currency = to_currency.get()
    input_amount = float(input_amount.get())
    if from_currency != 'EUR':
        input_amount = input_amount / rates[from_currency]
    output.insert(0, round(input_amount * rates[to_currency], 2 ))
    return

convert_button = tk.Button(window, text= "Конвертация", font="arial 16 bold" , borderwidth= 10, padx= 50, bg= "powder blue", command=lambda: currency_converter(form_currency ,to_currency,input_amount))
convert_button.grid(row = 3, columnspan=2)

window.mainloop()