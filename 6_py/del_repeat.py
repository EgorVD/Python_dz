from itertools import groupby

def main():
    """Функция удаляет повторы из списка"""
    while True:
        mass = input('Введите элементы списка через пробел ничего для выхода \n: ')
        if not mass:
            print('До свидания!')
            break
        else:
            mass = mass.split(' ')
            new_mass = [el for el, _ in groupby(mass)]
            print('Мы удалили повторы: ', new_mass)


if __name__ == "__main__":
    main()