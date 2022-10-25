N = str(int(input('Введите четырехзначное число: ')))
s = input('Введите одно из трех ключевых слов (usr, clc, adm): ')
if len(N + s) != 7:
    print('Ошибка при введении данных')
else:
    print('Ключ действия:', N + s)
    if 'usr' in (N + s):
        a = int(input('Подтвердите свой id-номер: '))
        if a == N:
            print('Пользователь подтвержден')
        else:
            print('Неверный id-номер')
    if 'clc' in (N + s):
        b = float(input('Введите 3 числа:\n'))
        c = float(input())
        d = float(input())
        print('Произведение модулей =', abs(b) * abs(c) * abs(d))
        print('Сумма чисел =', b + c + d)
        print('Наибольшее =', max(b, c, d))
        print('Наименьшее =', min(b, c, d))
        print('Деление =', round(max(b, c, d) / min(b, c, d), 5))
        if c < b < d or d < b < c:
            print('Вычитание =', round(max(b, c, d) - min(b, c, d) - b), 2)
        elif b < c < d or d < c < b:
            print('Вычитание =', round(max(b, c, d) - min(b, c, d) - c), 2)
        else:
            print('Вычитание =', round(max(b, c, d) - min(b, c, d) - d, 2))
    if 'adm' in (N + s):
        f = input('Введите строку: ')
        if len(f) >= 5 and ('.exe' or '.cmd' in f):
            print('Исполняемое действие')
        else:
            print('Неисполняемое действие')
