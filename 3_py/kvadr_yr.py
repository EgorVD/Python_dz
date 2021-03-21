def diskriminant(a, b, c):
    """Функция для подсчета дискриминанта

    Args:
        a (float): коэфиицент а
        b (float): коэфиицент b
        c (float): коэфиицент c

    Returns:
        float: результат вычисления дискриминанта
    """
    disk = b**2 - 4 * a * c
    return disk


def bol_null(b, a, c, disk):
    """Функция для нахождения корней при дискриминанте больше нуля

    Args:
        a (float): коэфиицент а
        b (float): коэфиицент b
        c (float): коэфиицент c
        disk (float): дискриминант

    Returns:
        [tuple]: кортеж содержащий корни уравнения x1 и x2
    """
    x1 = (-b - (diskriminant(a, b, c))**0.5) / (2 * a)
    x2 = (-b + (diskriminant(a, b, c))**0.5) / (2 * a)
    return x1, x2  


def men_null(b, a, c, disk):  # считаем комплексные корни
    """Функция для нахождения корней при дискриминанте меньше нуля

    Args:
        a (float): коэфиицент а
        b (float): коэфиицент b
        c (float): коэфиицент c
        disk (float): дискриминант

    Returns:
        [tuple]: кортеж содержащий корни уравнения x1 и x2
    """
    x1 = (-b - 1j * (abs(diskriminant(a, b, c)))**0.5) / (2 * a)
    x2 = (-b + 1j * (abs(diskriminant(a, b, c)))**0.5) / (2 * a)
    return x1, x2


def ravno_null(b, a):  # дискриминант 0
    """Функция для нахождения корней при дискриминанте равном нулю

    Args:
        a (float): коэфиицент а
        b (float): коэфиицент b

    Returns:
        [float]: корень уравнения x
    """
    x = -b / (2 * a)
    x = round(x, 3)
    return x