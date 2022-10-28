L = input('Введите строку: ')
if 3 <= len(L) <= 7:
    print('Множество 1')
    a = float(input('Введите число:\n'))
    b = float(input())
    c = float(input())
    d = float(input())
    print('max =', max(a, b, c, d))
    print('min =', min(a, b, c, d))
    s = 1
    if a != max(a, b, c, d) and a != min(a, b, c, d):
        s *= a
    if b != max(a, b, c, d) and b != min(a, b, c, d):
        s *= b
    if c != max(a, b, c, d) and c != min(a, b, c, d):
        s *= c
    if d != max(a, b, c, d) and d != min(a, b, c, d):
        s *= d
    print('result =', s)
if 10 < len(L) <= 15:
    print('Множество 2')
    h = str(len(L)**(len(L)-8))
    print(h)
    if len(h) == 6:
        print(max(h))
if 20 <= len(L) <= 30:
    m = input('Введите строку')
    if ('до' or 'ре') in m:
        print('Музыкальная пауза!')
    else:
        print('Чайная пауза!')
if len(L) < 3 or 7 < len(L) < 10 or 15 < len(L) < 20 or len(L) > 30:
    print('Строка не попала в множество!')
