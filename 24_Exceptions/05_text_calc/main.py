result = 0

with open('calc.txt', 'r') as calc_file:
    for i_line in calc_file:
        try:
            i_list = i_line.split()
            if len(i_list) != 3:
                raise IndexError
            number_1 = int(i_list[0])
            number_2 = int(i_list[2])
            if not isinstance(number_1, int) or not isinstance(number_2, int):
                raise ValueError
            action = i_list[1]
            if action == '+':
                result += number_1 + number_2
            elif action == '-':
                result += number_1 - number_2
            elif action == '*':
                result += number_1 * number_2
            elif action == '**':
                result += number_1 ** number_2

            try:
                if action == '/':
                    result += number_1 / number_2
                if action == '//':
                    result += number_1 // number_2
                if action == '%':
                    result += number_1 % number_2
            except ZeroDivisionError:
                print('На ноль делить нельзя!')

        except IndexError:
            print('Строка состоит не из трёх символов.')

        except ValueError:
            print('Невозможно преобразовать символ к целому числу.')

        except ZeroDivisionError:
            print('На ноль делить нельзя!')

    print('Сумма результатов -', result)
