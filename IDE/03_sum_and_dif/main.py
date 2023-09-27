def summa(n):
  summ = 0
  while n != 0:
    summ += n % 10
    n = n // 10
  return summ

def quantity(k):
  count = 0
  while k != 0:
    k = k // 10
    count += 1
  return count

number = int(input('Введите число - '))

sum_of_digits = summa(number)
print('\nСумма цифр -', sum_of_digits)

number_of_digits = quantity(number)
print('Количество цифр в числе -', number_of_digits)

difference = sum_of_digits - number_of_digits
print('Разность суммы и количества цифр -', difference)
