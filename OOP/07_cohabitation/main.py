import random


class Person:

    def __init__(self, name, satiety, home):
        self.name = name
        self.satiety = satiety
        self.home = home

    def print_info(self):
        print(
            '{}, сытость - {}, количество еды - {}, количество денег - {}'.format(
                self.name, self.satiety, self.home.food, self.home.money
            )
        )

    def to_act(self):

        action = random.randint(1, 6)

        if self.satiety < 0:
            raise SystemError('Ошибка!')
        elif 0 <= self.satiety < 20:
            self.to_eat()
        elif self.home.food < 10:
            self.shopping()
        elif self.home.money < 50:
            self.to_work()
        elif action == 1:
            self.to_work()
        elif action == 2:
            self.to_eat()
        else:
            self.to_play()
        self.print_info()

    def to_eat(self):
        print('\nКУШАЕМ')
        self.satiety += 1
        self.home.food -= 1

    def to_work(self):
        print('\nРАБОТАЕМ')
        self.home.money += 1
        self.satiety -= 1

    def to_play(self):
        print('\nИГРАЕМ')
        self.satiety -= 1

    def shopping(self):
        print('\nИДЁМ В МАГАЗИН')
        self.home.food += 1
        self.home.money -= 1


class House:

    def __init__(self, food, money):
        self.food = food
        self.money = money


try:
    my_home = House(50, 0)

    person_1 = Person('Артём', 50, my_home)
    person_1.print_info()

    person_2 = Person('Мария', 50, my_home)
    person_2.print_info()

    people = [person_1, person_2]

    for _ in range(365):
        for i_person in people:
            i_person.to_act()

    print('\nПрошёл год! Всё в порядке!')

except SystemError:
    print('Окончание работы программы!.')

