def vklad(mount, money, percent):
    """ Функция для подсчета денег в копилке после определенного срока

    Args:
        mount (int): Срок вклада
        money (int): Размер взноса
        percent (int): Процент по вкладу

    Returns:
        float: Сумма денег на вкладе в итоге
    """
    sch = 0
    while sch != mount:
        if sch == 0:  # после открытия вклада только вносим деньги проценты не начисляем
            total_money = money
        elif sch == mount:  # последний месяц не вносим, тольок начисляем процент
            total_money = total_money * percent

        total_money = money + total_money * percent
        sch += 1
    total_money = round(total_money, 2)
    return total_money - money  # костыль


def main():
    while True:
        x = input(
            'Для подсчета средств в копилке нажмите ENTER, для выхода напишите Выход \n')
        x = x.lower()
        if x == '':
            try:
                mount = int(input('Введите количество месяцев: '))
                money = int(input('Введите ежемесячный взнос: '))
                percent = int(input('Введите процент начисляемый на вклад: '))
                if mount == 0 or money == 0 or percent == 0:
                    print('Не вводите нули пожалуйса!')
                    continue
            except (ValueError, TypeError):
                print('Пожалуйста вводите числа')
                continue
            percent = percent / 100 + 1
            money_t = vklad(mount, money, percent)
            money_t = str(money_t).split('.')
            print(
                f'Количество денег на вкладе после {mount} месяцев {money_t[0]} рублей {money_t[1]} копеек\n')
        elif x == 'выход':
            break
        else:
            print('Повторите пожалуйста!')
        continue


if __name__ == "__main__":
    main()