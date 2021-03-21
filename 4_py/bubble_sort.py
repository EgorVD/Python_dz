def bubble_sort(mass):
    """ Функция которая сортируем массив пузырьком

    Args:
        mass (list): неотсортированный массив

    Returns:
        mass (list): отсортированный массив
    """
    N = len(mass)
    for i in range(1, N):
        for j in range(0, N - i):
            if ord(mass[j]) > ord(mass[j + 1]):
                mass[j], mass[j + 1] = mass[j + 1], mass[j]
    return mass


def main():
    print('Запускаю сортировку пузырьком!')
    while True:
        mass = input('Введите что-то или ничего для выхода \n: ')
        if not mass:
            print('До свидания!')
            break
        else:
            mass = mass.replace(' ', '')
            mass = list(mass)
            print('Так выглядит неотсортированный массив: ', mass)
            print('Так выглядит отсортированный массив: ', bubble_sort(mass))


if __name__ == "__main__":
    main()