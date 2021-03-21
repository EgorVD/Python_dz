from functools import reduce

def main():
    """ Функция для подсчета символов в тексте """
    
    text = print('Для выхода напишите "Bыход" ')
    while text != 'выход':
        text = input('Введите текст пожалуйста: ')
        text = text.lower()

        slov = list(map(lambda x: {x: text.count(x)}, set(text)))

        slov = str(slov)
        slov = slov.replace(
            '}',
            '').replace(
            '{',
            '').replace(
                "'",
                '').replace(
                    ' ',
                    '').replace(
                        '[',
                        '').replace(
                            ']',
            '')
        slov = slov.split(',')
        for i in slov:
            print(i)


if __name__ == "__main__":
    main()