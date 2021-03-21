def fact(a): return 1 if a < 1 else fact(a - 1) * a


while True:
    print('Вас приветствует программа для подсчета факториала!')
    a = input('Bведите целое число или ничего для выхода: ')
    if a == '':
        break
    try:
        a = int(a)
    except (ValueError, TypeError):
        print('Пожалуйста введите целое число')
        continue
    print(f'Факториал числа {a} равен {fact(a)}')
