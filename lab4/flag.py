

def hill_climbing(pos):
    curr_value = pos.value()
    while True:
        move, new_value = pos.best_move()
        if new_value >= curr_value:
            # no improvement, give up
            return pos, curr_value
        else:
            # position improves, keep searching
            curr_value = new_value
            pos.make_move(move)


class NQPosition:
    def __init__(self, N):
        self.N = N
        queen_locations = [-1 for x in range(N)]
        for i in range(N):
            queen_locations[i] = i

        print(queen_locations)

    # choose some internal representation of the NxN board
    # put queens on it

    def value(self):
        print("hey")
        # calculate number of conflicts (queens that can capture each other)
        value = 0
        
        return value

    def make_move(self, move):
        print("hey")
        # actually execute a move (change the board)

    def best_move(self):
        print("hey")
        # find the best move and the value function after making that move
        #return move, value


if __name__ == '__main__':
    NQPosition(4)

