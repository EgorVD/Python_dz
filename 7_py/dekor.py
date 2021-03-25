import time

def counter(func_to_decor):
    func_to_decor.cnt = 0 
    def count(a):
        func_to_decor(a)
        func_to_decor.cnt += 1
        print(f'Функция была вызвана {func_to_decor.cnt} раз')
    return count


def benchmark(func_to_decor):
    def bench(a):
        ts = time.time()
        func_to_decor(a)
        print('Функция отработала за: ', time.time()-ts)
    return bench

def logger(func_to_decor):
    def logg():
        pass

@counter
@benchmark
def prostoe(a):
    """Функция проверяет является ли число простым

    Args:
        a (int): число проверяемое на простоту

    Returns:
        string: сообщаем является ли число простым
    """
    deli = 2
    sch = 0
    while deli < a:
        if a % deli == 0:  # как только находится ещё одно число кроме 1 и a на которое делится а, прервыаем выполнение
            return print('Составное число')
        else:
            deli += 1
    return print('Простое число')