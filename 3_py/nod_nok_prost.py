def prostoe(a):
    """Функция проверяет является ли число простым

    Args:
        a (int): число проверяемое на простоту

    Returns:
        string: сообщаем является ли число простым
    """
    deli = 2
    sch = 0
    while deli < a:
        if a % deli == 0:  # как только находится ещё одно число кроме 1 и a на которое делится а, прервыаем выполнение
            return 'Составное число'
        else:
            deli += 1
    return 'Простое число'


def nod(a, b):
    """Функция находит наибольший общий делитель двух чисел

    Args:
        a (int): первое число
        b (int): вторе число

    Returns:
        int: наименьший общий делитель
    """
    return a if b == 0 else nod(b, a % b)


def nok(a, b):
    """Функция находит наименьшее общее кратное двух чисел

    Args:
        a (int): первое число
        b (int): вторе число

    Returns:
        int: наименьшее общее кратное
    """
    nok = (a * b) / nod(a, b)  # этой формулой нок связан с нод
    return nok





def loop():
    print('Привет, я умею находить НОД, НОК и проверять является ли число простым!')
    exi_t = input('Чего изволите? Введите: Нок, Нод или Простота или Выход: ')
    exi_t = exi_t.lower()
    if exi_t == 'нок':
        try:
            a = int(input('Введите первое число: '))
            b = int(input('Введите второе число: '))
        except ValueError:
            print('Похоже вы вводите не цифры!')
            loop()
        if a == 0 or b == 0:
            print('Не вводите нули пожалуйста!')
            loop()
        print('НОK равен: ', nok(a, b))
        loop()
    elif exi_t == 'нод':
        try:
            a = int(input('Введите первое число: '))
            b = int(input('Введите второе число: '))
        except ValueError:
            print('Похоже вы вводите не цифры!')
            loop()
        if a == 0 or b == 0:
            print('Не вводите нули пожалуйста!')
            loop()
        print('НОД равен: ', nod(a, b))
        loop()
    elif exi_t == 'простота':
        try:
            a = int(input('Введите число: '))
        except ValueError:
            print('Похоже вы вводите не цифры!')
            loop()
        if a == 0:
            print('Не вводите нули пожалуйста!')
            loop()
        print(prostoe(a))
        loop()
    elif exi_t == 'выход':
        quit()
    else:
        print('Не понимаю, повторите пожалуйста')
        loop()


if __name__ == "__main__":
    loop()
