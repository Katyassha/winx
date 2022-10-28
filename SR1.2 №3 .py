s = input('Введите натуральное трехзначное число: ')
b = max(s)
c = min(s)
b1 = s.replace(b, '', 1)
d = b1.replace(c, '', 1)
if int(b) - int(c) == int(d):
    if 150 < int(d) * int(b) * int(c) < 400:
        k = input('Это число интересное и магическое! Введите строку: ')
        g = float(input('Введите вещественное число: '))
        print('X = ', round((3 * (g - len(k)) ** 2) / (g * len(k)), 5))
    else:
        e = input('Это число интересное! Введите строку: ')
        print((int(s) / len(e))**2)
elif 150 < (int(d) * int(b) * int(c)) < 400:
    f = input('Это число магическое! Введите строку: ')
    if 'маг' in f:
        print('Заколдовано!')
    else:
        print('Нет эффекта!')
else:
    print('Это обычное число')
