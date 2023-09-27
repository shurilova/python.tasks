def lst_of_numbers(num):
    if num == 1:
        return 1, print(num)
    return lst_of_numbers(num - 1), print(num)


number = int(input('Введите число - '))
lst_of_numbers(number)
