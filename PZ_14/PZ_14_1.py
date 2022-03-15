#  В исходном текстовом файле (Dostoevsky.txt) найти все годы деятельности писателя
#  (например, 1821 года, 1837 год, 1843 году и так далее по всему тексту)
#  Посчитать количество полученных элементов.
import re

with open('Dostoevsky.txt', 'r', encoding='utf-8') as file:
    result = re.findall('\d{4}', file.read())
print('Годы деятельности писателя:', *result)
print(f'Количество годов деятельности Достоевского: {len(result)}')
