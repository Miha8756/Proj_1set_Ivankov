# Даны два целых числа A и B (A < B). Найти произведение всех целых чисел от A до B включительно
while True:  # Программа постоянно работает даже при ошибке
    try:  # Пользователь ввёл число
        print('Введите 2 числа, где первое меньше второго.')
        A = int(input('Введите первое число: '))
        B = int(input('Введите второе число: '))
        if A < B:
            break
        else:
            print('Вы ввели не числа, или вы ввели числа, где A > B, пожалуйста, введите заново числа. ')
    except ValueError:  # Человек ввёл не числа
        print('Вы ввели не числа, пожалуйста, введите числа.')
K = 1  # Счётчик произведения цифр
while A - 1 < B:  # Проходит от первого до последнего числа включительно
    K *= A  # Умножение каждого числа друг на друга
    A += 1  # Счётчик
print(K)  # Вывод произведения
print('Программа успешно завершена!')
