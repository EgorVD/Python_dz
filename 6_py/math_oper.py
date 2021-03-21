def plus(x, y):
    """ Функция складывает два числа

    Args:
        x (float): первое число
        y (float): вторе число

    Returns:
        float: результат
    """
    try:
        res = x + y
        return res
    except ValueError:
        return 'ERROR: "Вы делите на ноль!"'


def minus(x, y):
    """ Функция вычитает два числа

    Args:
        x (float): первое число
        y (float): вторе число

    Returns:
        float: результат
    """
    try:
        res = x - y
        return res
    except ValueError:
        return 'ERROR: "Вы делите на ноль!"'


def mnoj(x, y):
    """ Функция умножает два числа

    Args:
        x (float): первое число
        y (float): вторе число

    Returns:
        float: результат
    """
    try:
        res = x * y
        return res
    except ValueError:
        return 'ERROR: "Вы делите на ноль!"'


def ost_del(x, y):
    """ Функция находит остаток от деления двух числе

    Args:
        x (float): первое число
        y (float): вторе число

    Returns:
        float: результат
    """
    try:
        res = x % y
        return res
    except ZeroDivisionError:
        return 'ERROR: "Вы делите на ноль!"'


def cel_del(x, y):
    """ Функция делит нацело  два числа

    Args:
        x (float): первое число
        y (float): вторе число

    Returns:
        float: результат
    """
    try:
        res = x // y
        return res
    except ZeroDivisionError:
        return 'ERROR: "Вы делите на ноль!"'


def powe(a, b):
    """ Функция возводит число в степень

    Args:
        x (float): первое число
        y (float): вторе число

    Returns:
        float: результат
    """
    try:
        res = a ** b
    except OverflowError as exc:
        return 'ERROR: "Переполнение!"'
    return res


def delen(x, y):
    """ Функция делит два числа

    Args:
        x (float): первое число
        y (float): вторе число

    Returns:
        float: результат
    """
    try:
        res = x / y
        return res
    except ZeroDivisionError:
        return 'ERROR: "Вы делите на ноль!"'