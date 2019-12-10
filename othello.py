board = []
piece = ["x","o"]
turn = 0
for i in range(0,8): # adding all spaces on the board
    board.append([])
    for n in range(0,8):
        board[i].append(" ")
def move(prompt): # input returns a intiger without getting errors if you input letters.
    validinput = False
    while not validinput:
        a = input(prompt)
            if a.isdigit():
                b = int(a)
                if b > -1 and b < 8:
                    validinput = True
                    return b
                else:
                    print("input number between 0-7")
            else:
                print("input number")


def inspace(x,y):
    if board[y][x] == " ":          # empty space
        return 0
    elif board[y][x] == piece[turn]: #piece that belongs to current player
        return 1
    else:                           # piece belongs to opposite player
        return 2


def okmoveline(x,y):
    pass
def okmove(x,y):
    pass

def domoveline(x,y):
    pass
def domove(x,y):
    pass

board[4][4] = piece[0]
board[3][3] = piece[0]
board[4][3] = piece[1]
board[3][4] = piece[1]
game = True
while game:
    for i in range(0,8):
        print("|"+"|".join(board[i])+"|")
    #check if valid moves exist
    movedone = False
    while not movedone:
        print("Player",turn+1,piece[turn])
        x = move("x")
        y = move("y")
        if okmove(x, y):
            domove(x, y)
            movedone = True
        else:
            print("move doesnt change tiles")