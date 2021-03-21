import random

def main():
    """Функция считает частоту цифр в диапазоне чисел"""
    mass = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    vib = print('Попытаемся посчитать частоту использования цифр в диапазоне чисел')
    while vib != 'выход':
        vib = input('Начнем?/Выход?\n')
        vib = vib.lower()
        if vib == 'начнем' or vib == 'начнём':
            try:
                nd = int(input("Введите нижний предел диапазона: "))
                vd = int(input("Введите верхний предел диапазона: "))
            except ValueError:
                print('Вводите цифры пожалуйста!')
                continue
            sch = nd
            while sch < vd:
                x = random.randint(nd, vd)
                if x == 0:
                    mass[0] += 1
                elif x == 1:
                    mass[1] += 1
                elif x == 2:
                    mass[2] += 1
                elif x == 3:
                    mass[3] += 1
                elif x == 4:
                    mass[4] += 1
                elif x == 5:
                    mass[5] += 1
                elif x == 6:
                    mass[6] += 1
                elif x == 7:
                    mass[7] += 1
                elif x == 8:
                    mass[8] += 1
                elif x == 9:
                    mass[9] += 1
                sch += 1
                print(x)
            i = 0
            while i < 10:
                print('Цифра', i, 'повторяется {val} раз'.format(val=mass[i]))
                i += 1
            print('\n')
        elif vib == 'выход':
            print('До свидания!')
        else:
            print('Не понимаю, повторите.')


if __name__ == "__main__":
    main()