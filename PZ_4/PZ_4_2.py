# Спортсмен-лыжник начал тренировки, пробежав в первый день 10 км.
# Каждый следующий день он увеличивал длину пробега на P процентов от пробега предыдущего дня.
# (P - вещественное, 0 < P < 50)
# По данному P определить, после какого дня суммарный пробег лыжника за все дни превысит 200 км,
# и вывести найденное количество дней K (целое) и суммарный пробег S(вещественное число).
while True:  # Программа постоянно работает даже при ошибке
    try:  # Пользователь ввёл число
        P = int(input('Введите процент увеличения длины пробега лыжника (не больше 50%): '))
        if 0 < P < 50:  # ограничение по условию на входные данные
            break
        else:
            print('Вы ввели число >= 50 или <= 0, пожалуйста, введите заново число.')
    except ValueError:  # Человек ввёл не число
        print('Вы ввели не числа, пожалуйста, введите число.')
K = 1  # Счётчик дней
S = 10  # Счётчик пройденных километров
while S < 200:  # Пока длина пробега не привысит 200 км
    S += (S * P) / 100  # Находим процент от прошлой пройденной дистанции и прибавляем к пройденной дистанции
    K += 1  # Прибавляем дни
print(f'После {K} дня суммарный пробег лыжника превысит 200 км.')
print(f'Суммарный пробег лыжника равен {S}')
print('Программа успешно завершена!')

