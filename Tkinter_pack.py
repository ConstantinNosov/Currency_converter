from tkinter import *

#Создание главного окна в переменной root
root= Tk()

#Изменение заголовка окна
root.title("Конвертор валют")

#Создание виджетов Label для текстовых меток
label_1 = Label(root, text = "Введи сумму:" , font = "arial 12 bold", borderwidth = 10)
label_2 = Label(root, text = "Исходная валюта:" , font = "arial 10 bold", borderwidth = 10)
label_3 = Label(root, text = "Конвертируем в:" , font = "arial 10 bold", borderwidth = 10)
label_4 = Label(root, text = "Результат:" , font = "arial 10 bold", borderwidth = 10)
output = Label(root, text = "Введи значения:" , font = "arial 10 bold", borderwidth = 10)

#Создание виджетов
Enter_1 = Entry(root, borderwidth = 5)
Enter_2 = Entry(root, borderwidth = 5)
Enter_3 = Entry(root, borderwidth = 5)
my_button = Button(root, text = "Конвертация", font = "arial 10", borderwidth=5)

#Размещение виджетов в окне
label_1.pack()
label_2.pack()
label_3.pack()
label_4.pack()
output.pack()
Enter_1.pack()
Enter_2.pack()
Enter_3.pack()
my_button.pack()

#Бесконечный цикл 
root.mainloop()