def main():
    """ Функция для проверки корректности скобок """
    strok = input('Введите что-то со скобками: ')
    st_1 = []
    for i in strok:
        if i not in '()[]<>':
            continue
        if i in '([<':
            st_1.append(i)
        else:
            assert i in ')]>', 'ERROR'
            if len(st_1) == 0:
                print('Последовательность не верна!')
                exit()
            left = st_1.pop()
            if left == '(':
                right = ')'
            elif left == '[':
                right = ']'
            elif left == '<':
                right = '>'
            else:
                print('ERROR')
            if right != i:
                print('Последовательность не верна!')
                exit()
    if len(st_1) == 0:
        print('Последовательность верна!')
    else:
        print('Последовательность не верна!')
