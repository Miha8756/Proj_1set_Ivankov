print('5, 4, 3, 2, 1, -1, -2, -3, -4, -5', file=open('file7_1.txt', 'w'))
d, u = [int(i) for i in open('file7_1.txt').read().split(', ')], open('file_new7_1.txt', 'w')
a = [i for i in d if i > 0 if i % 2 == 0]
print('Исходные данные:', open('file7_1.txt').read(), file=u)
print('Количество элементов:', len(open('file7_1.txt').read().split(', ')), '\n', file=u)
print('Среднее арифметическое элементов:', sum(d) / len(d), '\n', file=u)
print('Положительные чётные элементы:', a, '\n', file=u)
print('Сумма положительных чётных элементов:', sum(a), '\n', file=u)
print('Среднее арифметическое положительных чётных элементов:', sum(a) / len(a), '\n', file=u)