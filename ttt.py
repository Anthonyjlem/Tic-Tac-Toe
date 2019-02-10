from tttlib import *

def main():
    T = genBoard()
    positions = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    player = int(input("Please choose what you are(1 = X, 2 = O): "))
    if player == 1:
        opponent = 2
    else:
        opponent = 1
    while True:
        printBoard(T)
        moveP = int(input("Choose a position: "))
        if moveP in positions:
            if T[moveP] == 0:
                T[moveP] = player
        state = analyzeBoard(T)
        if winner(state):
            return True
        moveO = genWinningMove(T,opponent)
        T[moveO] = opponent
        print("The computer chose", moveO)
        state = analyzeBoard(T)
        if winner(state):
            return True

if __name__ == "__main__":
    main()
