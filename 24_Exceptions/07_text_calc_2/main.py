def checks(string):
    n_1 = 0
    n_2 = 0
    act = ''
    try:
        i_list = string.split()
        if len(i_list) != 3:
            raise IndexError
        n_1 = int(i_list[0])
        n_2 = int(i_list[2])
        if not isinstance(n_1, int) or not isinstance(n_2, int):
            raise ValueError
        act = i_list[1]

    except IndexError:
        print('Строка состоит не из трёх символов.')

    except ValueError:
        print('Невозможно преобразовать символ к целому числу.')

    return n_1, n_2, act


def calculations(num_1, num_2, calc_action):
    # print(f'Запускаем calculations с {num_1}, {num_2}, {calc_action}')
    res = 0
    if calc_action == '+':
        res = num_1 + num_2
    elif calc_action == '-':
        res = num_1 - num_2
    elif calc_action == '*':
        res = num_1 * num_2
    elif calc_action == '**':
        res = num_1 ** num_2

    try:
        if calc_action == '/':
            res = num_1 / num_2
        elif calc_action == '//':
            res = num_1 // num_2
        elif calc_action == '%':
            res = num_1 % num_2
    except ZeroDivisionError:
        print('На ноль делить нельзя!')

    return res


result = 0
arithmetic_operations = '+-*/%**//'

with open('calc.txt', 'r') as calc_file:
    for i_line in calc_file:
        number_1, number_2, action = checks(i_line)

        if action not in arithmetic_operations:
            print('Обнаружена ошибка в строке {}.'.format(i_line.rstrip('\n')))
            answer = input('Хотите исправить? ')
            if answer.lower() == 'да':
                # print('Ввели ДА!')
                corrected_line = input('Введите исправленную строку - ')
                number_1, number_2, action = checks(corrected_line)
            elif answer.lower() == 'нет':
                # print('Ввели НЕТ!')
                continue
            else:
                print('Необходимо ввести Да или Нет.')

        result += calculations(number_1, number_2, action)

    print('Сумма результатов -', result)

