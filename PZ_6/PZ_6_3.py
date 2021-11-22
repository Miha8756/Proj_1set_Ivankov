# Дан список размера N. Возвести в квадрат все его локальные минимумы
# Локальный минимум - число, которое будет меньше обоих из своих соседей.
import random
mas = []
a = []
k = 0
n = int(input('Введите количество чисел в списке: '))
for j in range(n):
    mas.append(random.randint(1, 100))
print(f'В список занеслось {n} случайных чисел: ')
print(*mas)
mas = [100] + mas + [100]
for i in range(1, len(mas) - 1):
    if mas[i] < mas[i - 1] and mas[i] < mas[i + 1]:
        a.append(mas[i])
b = mas.pop(0)
c = mas.pop()
print('В списке найдены следующие локальные минимумы: ')
print(*a)
print('Список с локальными минимумами возведенными в квадрат')
print(*mas)


