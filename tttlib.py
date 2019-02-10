import random

def error(T):
    if len(T) < 9 or len(T) > 9:
        return -1
    for value in range(0, 9 ,1):
        if T[value] < 0 or T[value] > 2:
            return -1
    return 0

def genNonLoser(T, player):
    if player == 1:
        opponent = 2
    else:
        opponent = 1
    copyT = list(T)
    for i in range(len(T)):
        if copyT[i] == 0:
            copyT[i] = opponent
            winner = analyzeBoard(copyT)
            if winner == opponent:
                return i
            else:
                copyT[i] = 0
    return genRandomMove(T, player)

def genWinningMove(T, player):
    problem = error(T)
    if problem == -1:
        return -1
    copyT = list(T)
    for i in range(len(T)):
        if copyT[i] == 0:
            copyT[i] = player
            winner = analyzeBoard(copyT)
            if winner == player:
                return i
            else:
                copyT[i] = 0
    return genNonLoser(T, player)

def genRandomMove(T,player):
    unoccupied = []
    for i in range(len(T)):
        if T[i] == 0:
            unoccupied += [i]
    move = random.choice(unoccupied)
    return move

def winner(state):
    if state == 1:
        print("X won!")
        return True
    elif state == 3:
        print("It's a draw!")
        return True
    elif state == 2:
        print("O won!")
        return True
    else:
        return False

def genBoard():
    return [0, 0, 0, 0, 0, 0, 0, 0, 0]

def printBoard(T):
    if len(T) < 9 or len(T) > 9:
        return False
    for element in T:
        if element < 0 or element > 2:
            return False
    board = []
    for i in range(len(T)):
        if T[i] == 0:
            board += str(i)
        elif T[i] == 1:
            board += "X"
        else:
            board += "O"
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---|---|---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---|---|---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    return True

def won(player, T):
    if T[0] == player and T[1] == player and T[2] == player:
        return True
    elif T[3] == player and T[4] == player and T[5] == player:
        return True
    elif T[6] == player and T[7] == player and T[8] == player:
        return True
    elif T[0] == player and T[3] == player and T[6] == player:
        return True
    elif T[1] == player and T[4] == player and T[7] == player:
        return True
    elif T[2] == player and T[5] == player and T[8] == player:
        return True
    elif T[0] == player and T[4] == player and T[8] == player:
        return True
    elif T[2] == player and T[4] == player and T[6] == player:
        return True
    else:
        return False

def analyzeBoard(T):
    if len(T) < 9 or len(T) > 9:
        return -1
    for value in range(9):
        if T[value] < 0 or T[value] > 2:
            return -1

    x_won = won(1, T)
    o_won = won(2, T)

    if x_won:
        return 1
    elif o_won:
        return 2
    else:
        unoccupied = 0
        for i in range(9):
            if T[i] == 0:
                unoccupied += 1
        if unoccupied > 0:
            return 0
        else:
            return 3
