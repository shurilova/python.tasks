def fibonacci(num):
    if num == 1 or num == 2:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)


num_pos = int(input('Введите позицию числа в ряде Фибоначчи - '))

result = fibonacci(num_pos)
print('Число -', result)
