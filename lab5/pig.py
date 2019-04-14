import random

AI = 0
PLAYER = 1

ROLL = 0
PASS = 1
dice_rolls = [1, 2, 3, 4, 5, 6]
chance = 3.5


def pig_game(ai_func):
    rolled = 0
    turn = PLAYER
    player_points = ai_points = 0

    while player_points < 100 and ai_points < 100:
        print("Your points", player_points,
              "AI points", ai_points,
              "holding", rolled)

        if turn == PLAYER:
            decision = ROLL
            if rolled > 0:
                s = input("Do you want to keep rolling (Y/n)? ")
                if len(s) > 0 and s[0].lower() == "n":
                    decision = PASS

            if decision == PASS:
                rolled = 0
                turn = AI
            else:
                dieroll = random.randint(1, 6)
                print("You rolled...", dieroll)
                if dieroll == 1:
                    player_points -= rolled  # lose all points again
                    rolled = 0
                    turn = AI
                else:
                    rolled += dieroll
                    player_points += dieroll

        else:
            decision = ai_func(turn, rolled, ai_points, player_points)
            if decision == PASS:
                print("-- AI decides to pass.")
                rolled = 0
                turn = PLAYER
            else:
                dieroll = random.randint(1, 6)
                print("-- AI rolled...", dieroll)
                if dieroll == 1:
                    ai_points -= rolled  # lose all points again
                    rolled = 0
                    turn = PLAYER
                else:
                    rolled += dieroll
                    ai_points += dieroll

    if player_points >= 100:
        print("You won!")
    elif ai_points >= 100:
        print("AI won.")


def dummy_ai(turn, rolled, my_points, opp_points):
    if rolled < 21:
        return ROLL
    else:
        return PASS


def minimax_ai(turn, rolled, my_points, opp_points):
    # this is the top level of search
    # we search all possible moves
    # (PASS and ROLL in case of the Pig game)
    # and pick the one that returns the highest minimax estimate
    best_move = None
    best_value = -2
    for roll in dice_rolls:
        new_opp_points = opp_points + roll
        v = exp_minimax(turn, rolled + roll, new_opp_points, my_points, 4)
        print(roll, v)
        if v > best_value:
            best_value = v
            best_move = roll
    print(best_value)
    return best_move


def exp_minimax(turn, chance, rolled, my_points, opp_points, depth):
    # update remaining depth as we go deeper in the search tree
    depth = depth - 1

    # case 1a: somebody won, stop searching
    # return a high value if AI wins, low if it loses.
    if my_points >= 100:
        return 1
    if opp_points >= 100:
        return -1
    # case 1b: out of depth, stop searching
    # return game state eval (should be between win and loss)
    if depth < 1:
        return 0

    # case 2: AI's turn (and NOT a chance node):
    # return max value of possible moves (recursively)
    if turn == AI:
        best_value = -2
        for roll in dice_rolls:
            new_opp_points = opp_points + roll
            v = exp_minimax(turn, rolled + roll, new_opp_points, my_points, 4)
            if v > best_value:
                best_value = v
        return best_value

    # case 3: player's turn:
    # return min value (assume optimal action from player)
    if turn == PLAYER:
        best_value = 2
        for roll in dice_rolls:
            new_my_points = my_points + roll
            v = exp_minimax(turn, rolled + roll, new_my_points, new_my_points, 4)
            if v < best_value:
                best_value = v
        return best_value

    # case 4: chance node:
    # return average of all dice rolls
    return chance


if __name__ == '__main__':
    # pig_game(dummy_ai)
    pig_game(minimax_ai)
