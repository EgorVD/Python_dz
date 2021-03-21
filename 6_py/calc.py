import math
import math_oper as mo


while True:
    print('''Вас приветствует калькулятор!
    Возможные действия:
    +   : Сложение
    -   : Вычитание
    *   : Умножение
    /   : Деление
    **  : Возведение в степень
    %   : Остаток от деления
    //  : Целочисленное деление
    sin : синус числа
    cos : косинус числа

    Пустой ввдод: Выход

    ''')

    x = input('Введите первое число: ')
    if x == '':
        break
    else:
        x = x.replace(',', '.')
        try:
            x = float(x)
        except ValueError:
            print('Вы ввели не число!')
            continue

    while True:
        oper = input('Введите знак операции: ')
        if oper == '':
            break

        elif oper == 'sin':
            res = math.sin(x)
            print(f'Результат:{res}')
        elif oper == 'cos':
            res = math.cos(x)
            print(f'Результат:{res}')

        elif oper in ['+', '-', '/', '//', '*', '%', '**']:
            try:
                y = float(input('Введите второе число: '))
            except (ValueError, TypeError):
                print('Пожалуйста вводите число!')
                continue

            if oper == '+':
                res = mo.plus(x, y)
                print(f'Результат:{res}')

            elif oper == '-':
                res = mo.minus(x, y)
                print(f'Результат:{res}')

            elif oper == '/':
                res = mo.delen(x, y)
                if isinstance(res, str):
                    print('Похоже вы поделили на ноль, начнём заново!\n')
                    break
                else:
                    print(f'Результат:{res}')

            elif oper == '*':
                res = mo.mnoj(x, y)
                print(f'Результат:{res}')

            elif oper == '**':
                res = mo.powe(x, y)
                if isinstance(res, str):
                    print('Похоже возникала ошибка переполнения, начнём заново!\n')
                    break
                else:
                    print(f'Результат:{res}')
            elif oper == '%':
                res = mo.ost_del(x, y)
                if isinstance(res, str):
                    print('Похоже вы поделили на ноль, начнём заново!\n')
                    break
                else:
                    print(f'Результат:{res}')

            elif oper == '//':
                res = mo.cel_del(x, y)
                if isinstance(res, str):
                    print('Похоже вы поделили на ноль, начнём заново!\n')
                    break
                else:
                    print(f'Результат:{res}')

            else:
                print('Ошибка считывания оператора, пожалуйста повторите ввод!')
                continue
            x = res
        else:
            print('Ошибка считывания оператора, пожалуйста повторите ввод!')
            continue
        x = res
