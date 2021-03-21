def factorial(a):
    """ Функция для подсчета факториала числа

    Args:
        a (int): число

    Returns:
        int:  факториал числа а
    """
    if a == 0:
        return 1
    ans = 1
    for i in range(1, a + 1, 1):
        ans = ans * i
        print(i)
    return ans

def main():
    while True:
        print('Вас приветствует программа для подсчета факториала')
        a = input('Bведите целое число или ничего для выхода: ')
        if a == '':
            break
        try:
            a = int(a)
            if a < 0:
                print('Пожалуйста введите не отрицательное число')
                continue
        except (ValueError, TypeError):
            print('Пожалуйста введите целое число')
            continue
        print(f'Факториал числа {a} равен {factorial(a)}')


if __name__ == "__main__":
    main()