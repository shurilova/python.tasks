print('Введите первую точку - ')
x1 = float(input('X: '))
y1 = float(input('Y: '))

print('\nВведите вторую точку - ')
x2 = float(input('X: '))
y2 = float(input('Y: '))

x_diff = x1 - x2
y_diff = y1 - y2

if x_diff == 0:
    print('Прямая, параллельная оси Y. Через такое уравнение выразить не получится.')
    k = 1
else:
    k = y_diff / x_diff

b = y2 - k * x2

if k == 1 and x_diff != 0:
    print('Уравнение прямой, проходящей через эти точки - ')
    print('y = x +', b)
elif x_diff != 0:
    print('Уравнение прямой, проходящей через эти точки - ')
    print('y = ', k, ' * x +', b)