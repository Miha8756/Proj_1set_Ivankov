#  Из предложенного текстового файла (text18-7.txt) вывести на экран его содержимое, количество букв
#  в нижнем регистре. Сформировать новый файл, в который поместить текст в стихотворной форме,
#  предварительно поставив последнюю строку между второй и третьей.
print(open('text18-7.txt').read() + str(sum(map(str.islower, open('text18-7.txt').read()))))
print('\n'.join(open('text18-7.txt').read().splitlines()[:2]), '\n' + open('text18-7.txt').read().splitlines()[-1],
      '\n' + '\n'.join(open('text18-7.txt').read().splitlines()[2:6]), file=open('new-text18-7.txt', 'w'))
