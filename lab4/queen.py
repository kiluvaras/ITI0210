import copy
import math


class NQPosition:
    def __init__(self, N):
        self.N = N
        self.queens = [None for i in range(N)]
        # for i in range(N):
        #     self.queens[i] = (i, i)
        #     self.queens[i] = i
        self.queens[0] = (0, 0)
        self.queens[1] = (1, 1)
        self.queens[2] = (2, 2)
        self.queens[3] = (3, 3)
        print(self.queens)

        # print(self.queens)
        # choose some internal representation of the NxN board
        # put queens on it

    def value(self, A):
        value = 0
        # print("hei")
        N = self.N
        # A = self.queens
        # board = [[0 for i in range(n)]for i in range(n)]
        # board = []
        # for i in range(n):
        #     board[self.queens[i]][i] = 1
        # print(board)

        # for i in range(N):
        #     for j in range(i + 1, N - 1):
        #         print()

        # for i in range(N - 1):
        #     for j in range(i + 1, N):
        #         q1 = A[i]
        #         q2 = A[j]
        #         if q1[0] == q2[0]:
        #             value += 1
        #         elif q1[1] == q2[1]:
        #             value += 1
        #         elif q1[0] + q1[1] == q2[0] + q2[1]:
        #             value += 1
        #         elif q1[0] - q1[1] == q2[0] - q2[1]:
        #             value += 1

        for i in range(N - 1):
            for j in range(i + 1, N):
                q1 = A[i]
                q2 = A[j]
                if q1[0] == q2[0]:
                    value += 1
                elif q1[1] == q2[1]:
                    value += 1
                    # else if (Math.abs(column - q.getColumn()) == Math.abs(row - q.getRow()))
                elif math.fabs(q1[0] - q2[0]) == math.fabs(q1[1] - q2[1]):
                    # print("diag fire!")
                    value += 1

        # calculate number of conflicts (queens that can capture each other)
        # print(value)
        return value

    def make_move(self, move):
        # print(self.queens)
        self.queens[move[0]] = (self.queens[move[0]][0] + move[1], self.queens[move[0]][1])
        # print("hei")
        # print(self.queens)
        # self.value()
        # actually execute a move (change the board)

    def best_move(self):
        best_value = self.value(self.queens)
        best_board = self.queens
        move = ()

        for i in range(self.N):
            for j in range(self.N):
                if self.queens[i] != j:
                    temp_board = copy.deepcopy(self.queens)
                    temp_board[i] = (j, i)
                    # print("siin")
                    # print(self.queens)
                    # print(self.value(), best_value)
                    if self.value(temp_board) < best_value:
                        best_value = self.value(temp_board)
                        best_board = temp_board
                        # self.queens = temp_board
                        move = (i, (self.queens[i][0] - j))
                        print("move: ", move)

        print("parim", best_value)
        print("move: ", move)
        print("board: ", best_board)
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
    # nq = NQPosition(4)
    # nq.value()

    pos = NQPosition(4)  # test with the tiny 4x4 board first
    print("Initial position value", pos.value(pos.queens))
    # pos.make_move((1, 2))
    # pos.make_move((2, -1))
    print("-----------------------------------------")
    pos.best_move()
    best_pos, best_value = hill_climbing(pos)
    print("Final value", best_value)
    # # if best_value is 0, we solved the problem
