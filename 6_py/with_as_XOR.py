import random

def xor_encryption(chek):
    """ Функция xor шифрования

    Args:
        chek ([type]): [description]

    Returns:
        При успешном выполнении пишет результат в файл, иначе 0
    """
    text = read_from_file()
    if chek == 1:
        key = input("Введите ключ (Enter - ключ сгенерируется автоматически):")
        if not key:
            key = "".join(
                random.choice(
                    "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                )
                for i in range(random.randint(1, len(text)))
            )
            print(f"Вы не ввели ключ, поэтому мы его придумали сами:\n{key}")
    elif chek == 2:
        key = input("Введите ключ:")
        if not key:
            print('Похоже вы не ввели ключ, мы не знаем, чем расшифровать!')
            return 0
    result = bytearray()
    if type(text) == str:
        text = bytearray(text, "utf-8")
    key = bytearray(key, "utf-8")

    for i in range(len(text)):
        result.append(text[i] ^ key[i % len(key)])
    #result = result.decode('utf-8')
    print('Результат шифрования записан в файл!')
    write_to_file(result)


def write_to_file(data, filename="./text.txt"):
    """ Функция записи в файл

    Args:
        data (bytearray): данные для записи
    """
    with open(filename, "rb") as f:
        f = open(filename, "wb")
        f.write(data)


def read_from_file(filename="./text.txt"):
    """ Функция чтения из файла """
    with open(filename, "rb") as f:
        data = f.read()
        return data


def main():
    vibor = print('Вас приветствует xor шифровальщик')
    while vibor != '0':
        print('''Введите:
            1 - для шифровки
            2 - для дешифровки
            0 - для выхода''')
        vibor = input(': ')
        vibor = vibor.lower()
        if vibor == '1':
            xor_encryption(1)
        elif vibor == '2':
            xor_encryption(2)
        elif vibor == '0':
            print('До свидания!')
        else:
            print('Не понимаю')


if __name__ == "__main__":
    main()