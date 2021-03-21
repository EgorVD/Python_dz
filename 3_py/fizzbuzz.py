import random

def main():
    """Функция решает задачу fizzbuzz"""
    while True:
        x = random.randint(0, 100)
        if x % 15 == 0:  # Если поставить проверку на кратность 15, после проверки на 3 или 5, то ни одного 'fizzbuzz' не увидим.
            print('fizzbuzz')
        elif x % 5 == 0:
            print('buzz')
        elif x % 3 == 0:
            print('fizz')
        print(x)


if __name__ == "__main__":
    main()