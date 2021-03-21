def svetofor(color):
    color = color.lower()  # переведем в нижний регистр вдруг кто-то напишет ЗеЛенЫй
    if color == 'зеленый' or color == 'зелёный':
        print('Иди!')
        return color
    elif color == 'желтый' or color == 'жёлтый':
        print('Приготовься!')
        return color
    elif color == 'красный':
        print('Стой!')
        return color
    elif color == 'выход':
        print('До свидания!')
        return color
    else:
        print('Не понимаю, повторите пожалуйста')
        return color


def main():
    color = print('Пора учить пдд!')
    while color != 'выход':
        color = input('Какой горит сигнал? ')  # Узнаем, что горит
        svetofor(color)


if __name__ == "__main__":
    main()
