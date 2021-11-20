def summa(n, m):
    n = a
    m = b
    s = 0
    while n - 1 < m:
        s += n
        n += 1
    return s


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print(f'Сумма чисел расположенных между {a} и {b} равно {summa(a, b)}')
