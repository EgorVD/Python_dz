import os
import kvadr_yr as ky

def repeat():
    print('\n')

    x = input('Посчитаем квадратные уравнения? Да/Нет? ')
    x = x.lower()

    if x == 'да':
        os.system('cls||clear')
        print('Поехали!')
        _input()

    elif x == 'нет':
        print('Bye Bye!')
        return 0

    else:
        repeat()  


def _input():
    print('\n')
    print('*ПОДСКАЗКА*')
    print('Квадратное уравнение это уравнение вида ax^2 + bx + c = 0, a не равно 0!')

    try:  # обработаем ввод не чисел
        a = float(input('Введите коэффицент а: ').replace(',', '.')) # заменbv запятые в на точку, чтобы избежать ошибки
        b = float(input('Введите коэффицент b: ').replace(',', '.'))
        c = float(input('Введите коэффицент c: ').replace(',', '.'))
        if a == 0:
            print(
                'Если а = 0, то уравнение не квадратное, а линейное! Но его я тоже могу решить.')
            x = -c / b
            x = round(x, 3)
            print('Корень равен х = ', x)
            _input()

    except ValueError:
        print('Похоже вы вводите не цифры!')
        _input()

    disk = ky.diskriminant(a, b, c)

    if disk == 0:
        print('Дискриминант = 0, тут все просто:')
        x = ky.ravno_null(b, a)  # получим значения корней
        print('Первый корень равен второму х = ', x)
        repeat()

    elif disk > 0:
        print('Дискриминант больше нуля:')
        korni = ky.bol_null(b, a, c, disk)  # получим значения корней
        x1 = korni[0]  # вытащим их из кортежа
        x2 = korni[1]
        x1 = round(x1, 3)
        x2 = round(x2, 3)
        print('Первый корень х1 = ', x1, 'Второй корень х2 = ', x2)
        repeat()

    else:
        print('Чтож дискриминант меньше нуля, придется посчитать комплексные числа ')
        korni = ky.men_null(b, a, c, disk)  # получим значения корней
        x1 = korni[0]  # вытащим их из кортежа
        x2 = korni[1]
        x1 = round(x1.real, 3) + round(x1.imag, 3) * 1j
        x2 = round(x2.real, 3) + round(x2.imag, 3) * 1j
        print('Первый корень х1 = ', x1, 'Второй корень х2 = ', x2)
        repeat()


if __name__ == "__main__":
    repeat()
