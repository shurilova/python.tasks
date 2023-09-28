class Board:

    def __init__(self, board):
        self.board = board

    def create_board(self):
        print('-' * 13)
        for i_num in range(3):
            print(
                '|', self.board[0 + i_num * 3],
                '|', self.board[1 + i_num * 3],
                '|', self.board[2 + i_num * 3],
                '|'
            )
            print('-' * 13)

    def check_winning(self):
        winning = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for i_line in winning:
            if self.board[i_line[0]] == self.board[i_line[1]] == self.board[i_line[2]]:
                return self.board[i_line[0]]
        return False


class Cell:

    def __init__(self, sign, board):
        self.sign = sign
        self.board = board

    def filling(self):
        fullness = False
        while not fullness:
            answer = int(input('В какую клетку ставим {}? '.format(self.sign)))
            if 1 <= answer <= 9:
                if str(self.board[answer - 1]) not in 'XO':
                    self.board[answer - 1] = self.sign
                    fullness = True
                else:
                    print('Эта клетка уже занята!')
            else:
                print('Некорректный ввод! Необходимо ввести число от 1 до 9.')


numbers = list(range(1, 10))

my_board = Board(numbers)

my_cell_x = Cell('X', numbers)
my_cell_0 = Cell('O', numbers)

count = 0

while True:

    my_board.create_board()

    if count % 2 == 0:
        my_cell_x.filling()
    else:
        my_cell_0.filling()
    count += 1

    if count > 4:
        result = my_board.check_winning()
        if result:
            my_board.create_board()
            print(result, 'выиграл!')
            break

    if count == 9:
        my_board.create_board()
        print('Ничья!')
        break
