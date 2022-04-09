#  В матрице элементы последнего столбца заменить на -1
from random import randint

#  Заносим в переменные параметры матрицы
m, n, y, z = [int(input(i)) for i in ("Количество строк = ", "Количество столбцов = ", "От = ", "До = ")]
#  заполняем матрицу случайными числами
matrix = [[randint(y, z) for _ in range(n)] for j in range(m)]
print('Исходная матрица:', '\n', [i for i in matrix])
#  цикл заменения последних элементов в строке на -1
for i in range(m):
    matrix[i][n - 1] = -1
print('Полученная матрица:', '\n', [i for i in matrix])
