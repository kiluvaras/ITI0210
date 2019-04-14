import copy
import math
from random import randint


class NQPosition:
    def __init__(self, N):
        self.N = N
        self.queens = [None for i in range(N)]
        for i in range(N):
            # (RIDA, VEERG)
            self.queens[i] = (randint(0, N - 1), i)
        print(self.queens)

        # print(self.queens)
        # choose some internal representation of the NxN board
        # put queens on it

    def value(self, board):
        value = 0
        N = self.N

        for i in range(N - 1):
            for j in range(i + 1, N):
                q1 = board[i]
                q2 = board[j]
                if q1[0] == q2[0]:
                    value += 1
                elif q1[1] == q2[1]:
                    value += 1
                elif math.fabs(q1[0] - q2[0]) == math.fabs(q1[1] - q2[1]):
                    # print("diag fire!")
                    value += 1

        # calculate number of conflicts (queens that can capture each other)
        # print(value)
        return value

    def make_move(self, move):
        self.queens[move[0]] = (self.queens[move[0]][0] + move[1], move[0])
        # self.value()
        # actually execute a move (change the board)

    def best_move(self):
        best_value = self.value(self.queens)
        best_board = self.queens
        move = ()

        for i in range(self.N):
            for j in range(self.N):
                # print("võrdlus:", self.queens[i], "-->", j)
                if self.queens[i][1] != j:
                    temp_board = copy.deepcopy(self.queens)
                    temp_board[i] = (j, i)
                    # print("siin")
                    # print(self.queens)
                    # print(self.value(), best_value)
                    if self.value(temp_board) < best_value:
                        best_value = self.value(temp_board)
                        best_board = temp_board
                        # self.queens = temp_board
                        # print("jama: ", self.queens[i][0], j)
                        move = (i, (j - self.queens[i][0]))
                        # print("move: ", move)

        print("algne board: ", self.queens)
        print("parim", best_value)
        print("move: ", move)
        print("board pärast: ", best_board)
        print("\n")
        return move, best_value
        # find the best move and the value function after making that move
        # return move, value


def hill_climbing(pos):
    curr_value = pos.value(pos.queens)
    while True:
        move, new_value = pos.best_move()
        if new_value >= curr_value:
            # no improvement, give up
            return pos, curr_value
        else:
            # position improves, keep searching
            curr_value = new_value
            pos.make_move(move)


if __name__ == '__main__':
    pos = NQPosition(4)  # test with the tiny 4x4 board first
    print("Initial position value", pos.value(pos.queens))
    pos.make_move((0, 1))
    print(pos.queens)
    pos.make_move((3, 3))
    print(pos.queens)
    print(pos.value(pos.queens))
    # pos.best_move()
    # pos.best_move()
    # pos.best_move()
    # best_pos, best_value = hill_climbing(pos)
    # print("Final value", best_value)
    # if best_value is 0, we solved the problem
