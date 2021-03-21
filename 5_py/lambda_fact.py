from functools import reduce

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
    fact = reduce(lambda y, x: y * x, range(1, a + 1))
    print(f'Факториал числа {a} равен {fact}')
