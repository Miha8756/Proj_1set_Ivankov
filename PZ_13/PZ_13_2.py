#  Составить генератор (yield), который преобразует все буквенные (заглавные) символы в строчные (маленькие).
def ll(stroka):
    yield from [i.lower() for i in stroka]


print(''.join(ll(input('Введите строку: '))))
