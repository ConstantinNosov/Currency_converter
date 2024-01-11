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


#Создание виджетов  для полей ввода
Enter_1 = Entry(root, borderwidth = 5)
Enter_2 = Entry(root, borderwidth = 5)
Enter_3 = Entry(root, borderwidth = 5)
output = Entry(root, text = "Введи значения:" , font = "arial 10 bold", borderwidth = 10)
my_button = Button(root, text = "Конвертация", font = "arial 10", borderwidth=5)


#Размещение виджетов в окне
label_1.grid(row=0, column=0)
label_2.grid(row=1, column=0)
label_3.grid(row=2, column=0)
label_4.grid(row=4, column=0)
Enter_1.grid(row=0, column=1)
Enter_2.grid(row=1, column=1)
Enter_3.grid(row=2, column=1)
my_button.grid(row=3, column= 0, columnspan=2)
output.grid(row=4, column=1)


#Бесконечный цикл 
root.mainloop()