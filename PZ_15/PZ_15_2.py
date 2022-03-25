#  В матрице элементы последнего столбца заменить на -1
from random import randint

m, n, y, z = [int(input(i)) for i in ("Количество строк = ", "Количество столбцов = ", "От = ", "До = ")]
matrix = [[randint(y, z) for _ in range(n)] for j in range(m)]
print('Исходная матрица')
for i in matrix:
    print(*i)
for i in range(m):
    matrix[i][n-1] = -1
print('Полученная матрица')
for i in matrix:
    print(*i)
