

def symb_of_text():
    """ Функция считате колличество вхождений символа в текст """
    slov = {}
    text = input('Введите текст пожалуйста: ')
    text = text.lower()
    for i in text:
        sch = 0
        sumb = i
        for j in text:
            if j == sumb:
                sch += 1
        slov['Символ_' + i] = '_встречается_' + str(sch) + '_раз'
    slov = str(slov)
    slov = slov.replace(
        '}',
        '').replace(
        '{',
        '').replace(
            "'",
            '').replace(
                ' ',
        '')
    slov = slov.split(',')
    for i in slov:
        print(i)


def slov_on_text():
    """ Функция считает слова в тексте

    Returns:
        int: колличество слов
    """
    text = input('Введите текст пожалуйста: ')
    text = text.lower()
    text = text.replace("\n", " ")
    text = text.replace(
        ",",
        "").replace(
        ".",
        "").replace(
            "?",
            "").replace(
                "!",
        "")
    slov = text.split()
    x = len(slov)
    return x


def predl_of_text():
    """ Функция считает предложения в тексте

    Returns:
        int: колличество предложений
    """
    text = input('Введите текст пожалуйста: ')
    text = text.lower()
    text = text.replace(" ", "").replace('\n', '')
    text = text.replace('!', 'Ǣ').replace('?', 'Ǣ').replace('.', 'Ǣ')
    text = text.split('Ǣ')
    while True:
        try:
            text.remove('')
        except ValueError:
            break
    x = len(text)
    return x

def main():
    while True:
        next_step = input(
            """
    Выберите задачу.
    Подсчет частоты вхождений символов в текст: 1
    Подсчет колличества слов в тексте:          2
    Подсчет колличества предложений в тексте:   3
    Выход:                                      Enter
    """
        )
        if not next_step:
            print("Увидимся...")
            break
        elif next_step == "1":
            symb_of_text()
        elif next_step == "2":
            print(f'В вашем тексте {slov_on_text()} слов')
        elif next_step == "3":
            print(f'В вашем тексте {predl_of_text()} предложений')
        else:
            print("Повторите ввод...")


if __name__ == "__main__":
    main()