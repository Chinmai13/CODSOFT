import math

board = [" "]*9

def print_board():
    for i in range(0,9,3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("---------")

def winner(b):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for x,y,z in wins:
        if b[x] == b[y] == b[z] and b[x] != " ":
            return b[x]
    return None

def minimax(b, depth, is_max):
    w = winner(b)
    if w == "O":
        return 1
    if w == "X":
        return -1
    if " " not in b:
        return 0
    if is_max:
        best = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                best = max(best, minimax(b, depth+1, False))
                b[i] = " "
        return best
    else:
        best = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                best = min(best, minimax(b, depth+1, True))
                b[i] = " "
        return best

def best_move():
    move = -1
    best = -math.inf
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best:
                best = score
                move = i
    board[move] = "O"

while True:
    print_board()
    pos = int(input("Enter position (0-8): "))
    if board[pos] != " ":
        continue
    board[pos] = "X"
    if winner(board) or " " not in board:
        break
    best_move()
    if winner(board) or " " not in board:
        break

print_board()
print("Winner:", winner(board))
