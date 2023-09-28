import random


class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return '{} {}'.format(self.rank, self.suit)

    def return_value(self):
        if self.rank in ['Валет', 'Дама', 'Король']:
            return 10
        elif self.rank == 'Туз':
            return 11
        else:
            return self.rank


class Deck:

    def __init__(self):
        ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Валет', 'Дама', 'Король', 'Туз']
        suits = ['крести', 'бубен', 'черви', 'пики']
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]

    def __str__(self):
        string = ''
        for i_elem in range(len(self.cards)):
            string += ' ' * i_elem + str(self.cards[i_elem]) + '\n'
        return string

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_deck(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None


class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []

    def __str__(self):
        string = '\nИгрок - {}\n'.format(self.name)
        for i_card in self.hand:
            string += str(i_card) + '\n'
        string += 'Сумма очков - ' + str(self.calculate_value())
        return string

    def draw(self, deck):
        self.hand.append(deck.draw_deck())
        return self

    def calculate_value(self):
        value = sum([card.return_value() for card in self.hand])
        if value > 21:
            for i_card in self.hand:
                if i_card.return_value() == 11:
                    value -= 10
                    if value <= 21:
                        break
        return value


class Game:

    def __init__(self, player):
        self.player = player

    def start(self):

        deck_of_cards = Deck()
        deck_of_cards.shuffle()

        self.player.draw(deck_of_cards).draw(deck_of_cards)

        computer = Player('Компьютер')
        computer.draw(deck_of_cards).draw(deck_of_cards)

        print('Раздаём карты -')
        print(self.player)

        if self.player.calculate_value() == 21 and computer.calculate_value() != 21:
            print(computer)
            print('\nКостя выиграл!')
        elif computer.calculate_value() == 21 and self.player.calculate_value() != 21:
            print(computer)
            print('\nКостя проиграл!')
        elif self.player.calculate_value() == 21 and computer.calculate_value() == 21:
            print(computer)
            print('\nНичья!')
        else:
            while True:
                choice = input('\nВзять карту или нет? ')
                if choice.lower() == 'да':
                    self.player.draw(deck_of_cards)
                    print(self.player)
                    if self.player.calculate_value() > 21:
                        print('\nКостя проиграл!')
                        break
                elif choice.lower() == 'нет':
                    print(computer)
                    player_value = self.player.calculate_value()
                    computer_value = computer.calculate_value()
                    if player_value == 21 or computer_value > 21 or player_value > computer_value:
                        print('\nКостя выиграл!')
                    elif computer_value == 21 or player_value > 21 or player_value < computer_value:
                        print('\nКостя проиграл!')
                    else:
                        print('\nНичья!')
                    break
                else:
                    print('\nНеобходимо ввести Да или Нет!')


player_1 = Player('Костя')
game = Game(player_1)
game.start()
