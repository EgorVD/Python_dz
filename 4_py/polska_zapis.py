def obr_pol_not(text):
    """ Функция для записи выражения в обратной польской нотации

    Args:
        text (str): исходный пример

    Returns:
        list: массив с примером записанный в обратной польской нотации
    """
    lex = in_put(text)
    s2 = []
    r = []
    oper = ["+", "-", "*", "/", "(", ")"]
    for a in lex:
        if a == "(":
            s2 = [a] + s2
        elif a in oper:
            if s2 == []:
                s2 = [a]
            elif a == ")":
                while(True):
                    q = s2[0]
                    s2 = s2[1:]
                    if q == "(":
                        break
                    r += [q]
            elif priority(s2[0]) < priority(a):
                s2 = [a] + s2
            else:
                while(True):
                    if s2 == []:
                        break
                    q = s2[0]
                    r += [q]
                    s2 = s2[1:]
                    if priority(q) == priority(a):
                        break
                s2 = [a] + s2
        else:
            r += [a]
    while(s2 != []):
        q = s2[0]
        r += [q]
        s2 = s2[1:]
    return r


def in_put(text):  # режем входящую строку
    """ Функция разделяющая строку на числа и операторы

    Args:
        text (string): исходная строка

    Returns:
        list: массив чисел и операторов
    """
    oper = ["+", "-", "*", "/", "(", ")"]
    mass = []
    tmp = ""
    for a in text:
        if a != " ":
            if a in oper:
                if tmp != "":
                    mass += [tmp]
                mass += [a]
                tmp = ""
            else:
                tmp += a
    if tmp != "":
        mass += [tmp]
    return mass


def priority(o):
    """ Функция определения приоритета оператора

    Args:
        o (string): оператор

    Returns:
        int: приоритет
    """
    if o == "+" or o == "-":
        return 1
    elif o == "*" or o == "/":
        return 2
    elif o == "(":
        return 0


def calc(x, y, oper):
    """ функция для проведения математической операции над двумя числами

    Args:
        x (int): первое число
        y (int): второе число
        oper (string): оператор

    Returns:
        int: результат операции
    """
    if oper == '+':
        return x + y
    elif oper == '-':
        return x - y
    elif oper == '*':
        return x * y
    else:
        return x / y


def reshenie(mass):
    """ Функция для решения примеров в обратной польской нотации

    Args:
        mass ([type]): [description]

    Returns:
        [type]: [description]
    """
    stack = []
    for item in mass:
        if item.isdigit() == True:
            stack.append(int(item))
        else:
            x = stack.pop()
            y = stack.pop()
            res = calc(y, x, item)
            stack.append(res)
    return stack.pop()

    return stack


def main():
    text = print('Вас приветствует калькулятор!')
    while text != '':
        text = input('Введите пример или ничего для выхода \n')
        if text != '':
            mass = obr_pol_not(text)
            res = reshenie(mass)
            print(f'Ответ: {res}')


if __name__ == "__main__":
    main()