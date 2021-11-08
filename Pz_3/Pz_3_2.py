# Единицы массы пронумерованы следующим образом
# 1 - килограмм, 2 - миллиграмм, 3 - грамм, 4 - тонна, 5 - центнер
# Данн номер единицы массы(целове число в диапазоне 1 - 5) и длина отрезка в этих единицах(вещественное число)
# Найти массу тела в килограммах.
while True:  # Программа постоянно работает даже при ошибке
    try:  # Пользователь ввёл числа
        print('Введите единицы измерения массы от 1 до 5:')
        print('1 - килограмм')
        print('2 - миллиграмм')
        print('3 - грамм')
        print('4 - тонна')
        print('5 - центнер')
        A = int(input())
        B = float(input('Введите длину отрезка в этих единицах: '))
        if A == 1:  # Выводим килограммы
            print('Масса тела в килограммах = ', B)
        elif A == 2:  # Переводим миллиграммы в килограммы
            print('Масса тела в килограммах = ', B / 1000000)
        elif A == 3:  # Переводим граммы в килограммы
            print('Масса тела в килограммах = ', B / 1000)
        elif A == 4:  # Переводим тонны в килограммы
            print('Масса тела в килограммах = ', B * 1000)
        else:  # Переводим центнеры в килограммы
            print('Масса тела в килограммах = ', B * 100)
        break
    except ValueError:
        print('Вы ввели не числа, пожалуйста введите числа.')
print('Программа успешно завершена!')
