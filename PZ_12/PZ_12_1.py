#  В соответствии с номером варианта перейти по ссылке на прототип.
#  Реализовать его в IDE PyCharm Community с применением пакета tk.
#  Получить интерфейс максимально приближенный к оригиналу (см. таблицу 1).
from tkinter import *
from tkinter.ttk import Combobox

root = Tk()
#  Создание окна размером 811х499
root.geometry('811x499')
#  Называем окно "Отправка формы"
root.title('Отправка формы')
#  Задаем цвет фона окна
root['bg'] = '#4bb4c2'

#  Выводим текст с фоном 4bb4c2, белым шрифтом Arial 17 пунктов, с расположением координат (100;20)
Label(text='Contact form', bg='#4bb4c2', fg='white', font='Arial 17').place(x=100, y=20)
#  Выводим текст с фоном 4bb4c2, белым шрифтом Arial 10 пунктов, с расположением координат (104;55) с 50 шириной
Label(text='Please fill in your information and well be sending your order in no time', width=50, bg='#4bb4c2',
      fg='white', font='Arial 10').place(x=104, y=55)

#  Выводим текст с фоном 4bb4c2, белым шрифтом Arial 12 пунктов, с расположением координат (100;120)
Label(text='Your Name', bg='#4bb4c2', fg='white', font='arial 12').place(x=100, y=120)
#  Создаем поле для ввода, в котором будет написано 'First Name' серым цветом Arial 12,
#  15 ширины, 2 толщиной границы с расположением координат (260;120)
Entry(textvariable=StringVar(value='First Name'), fg='#999', width=15, bd='2', font='Arial 12').place(x=260, y=120)
#  Создаем поле для ввода, в котором будет написано 'Last Name' серым цветом Arial 12,
#  15 ширины, 2 толщиной границы с расположением координат (420;120)
Entry(textvariable=StringVar(value='Last Name'), fg='#999', width=15, bd='2', font='Arial 12').place(x=420, y=120)

#  Выводим текст с фоном 4bb4c2, белым шрифтом Arial 12 пунктов, с расположением координат (100;160)
Label(text='Your Email', bg='#4bb4c2', fg='white', font='Arial 12').place(x=100, y=160)
#  Создаем поле для ввода, в котором будет написано 'e.d.hello@contact.net' серым цветом Arial 12,
#  33 ширины, 2 толщиной границы с расположением координат (260;160)
Entry(textvariable=StringVar(value='e.d.hello@contact.net'), fg='#999', width=33, bd='2', font='Arial 12').place(x=260,
                                                                                                                 y=160)
#  Выводим текст с фоном 4bb4c2, белым шрифтом Arial 12 пунктов, с расположением координат (100;200)
Label(text='Phone', bg='#4bb4c2', fg='white', font='Arial 12').place(x=100, y=200)
#  Создаем поле для ввода, в котором будет написано '###' серым цветом Arial 12,
#  9 ширины, 2 толщиной границы с расположением координат (260;200)
Entry(textvariable=StringVar(value='###'), fg='#999', width=9, bd='2', font='Arial 12').place(x=260, y=200)
#  Создаем поле для ввода, в котором будет написано '###' серым цветом Arial 12,
#  9 ширины, 2 толщиной границы с расположением координат (366;200)
Entry(textvariable=StringVar(value='###'), fg='#999', width=9, bd='2', font='Arial 12').place(x=366, y=200)
#  Создаем поле для ввода, в котором будет написано '###' серым цветом Arial 12,
#  9 ширины, 2 толщиной границы с расположением координат (475;200)
Entry(textvariable=StringVar(value='###'), fg='#999', width=9, bd='2', font='Arial 12').place(x=475, y=200)

#  Выводим текст с фоном 4bb4c2, белым шрифтом Arial 12 пунктов, с расположением координат (100;240)
Label(text='Message Subject*', bg='#4bb4c2', fg='white', font='Arial 12').place(x=100, y=240)
#  Используем функцию Combobox для создания поля для вывода и выбора различных вариантов ответа
#  шириной 28 и вариантом ответа 'Other'
combo = Combobox(root, width=28, values=['Other'])
#  Делаем вариант ответа 'Other' приоритетным (чтобы он выводился сразу в поле, а только потом другие варианты)
combo.current(0)
#  Располагаем поле на координатах (260;240)
combo.place(x=260, y=240)

#  Выводим текст с фоном 4bb4c2, белым шрифтом Arial 12 пунктов, с расположением координат (100;280)
Label(text='Message*', bg='#4bb4c2', fg='white', font='Arial 12').place(x=100, y=280)
#  Создаем пустое поле для ввода, в котором пользователь пишет серым цветом Arial 38,
#  11 ширины, 2 толщиной границы с расположением координат (260;280)
Entry(fg='#999', width=11, bd='2', font='Arial 38').place(x=260, y=280)

#  Выводим текст с фоном 4bb4c2, белым шрифтом Arial 12 пунктов, с расположением координат (100;370)
Label(text='Verification*', bg='#4bb4c2', fg='white', font='Arial 12').place(x=100, y=370)
#  Создание прямоугольника высотой 45, шириной 170 с расположением координат (260;370)
Canvas(root, bg='#fff', height=45, width=170).place(x=260, y=370)
#  Создание квадрата высотой 25, шириной 25 с расположением координат (270;380)
Canvas(root, bg='#fff', height=25, width=25).place(x=270, y=380)

#  Создаем кнопку "SUBMIT FORM", 18 ширины белого цвета с фоном #4bb4c2, с расположением координат (100;450)
Button(text="SUBMIT FORM", width=18, fg='white', bg='#4bb4c2').place(x=100, y=450)

#  Выводим окно
root.mainloop()
