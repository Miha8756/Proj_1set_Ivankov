#  В матрице элементы строки N (N задать с клавиатуры) увеличить на 3
from random import randint

m, n, y, z, g = [int(input(i)) for i in ("Количество строк = ", "Количество столбцов = ", "От = ", "До = ", "Строка = ")]
matrix = [[randint(y, z) for _ in range(n)] for j in range(m)]
print('Исходная матрица')
for i in matrix:
    print(*i)
u = []
for i in matrix[g - 1]:
    u.append(i + 3)
matrix[g - 1] = u
print('Полученная матрица')
for i in matrix:
    print(*i)
