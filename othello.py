board = []
piece = ["x","o"]
turn = 0
points = [0, 0]
for i in range(0,8): # adding all spaces on the board
    board.append([])
    for n in range(0,8):
        board[i].append(" ")
def move(prompt): # input returns a intiger without getting errors if you input letters
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
    elif board[y][x] == piece[turn]: # piece that belongs to current player
        return 1
    else:                           # piece belongs to opposite player
        return 2


def okmoveline(x,y,fx,fy):  # checks if any pieces can be flipped in a line
    loop = True
    line = False
    x += fx
    y += fy
    while loop and x < 8 and x > -1 and y < 8 and y > -1:
        if 0 == inspace(x, y):
            loop = False
            return False
        elif 1 == inspace(x, y):
            loop = False
            if line:
                return True
            else:
                return False
        else:
            line = True
        x += fx
        y += fy
    return False

def okmove(x,y):    # checks if the current player can put a piece in the position
    returnvalue = False
    for fx in range(-1,2):
        for fy in range(-1,2):
            if okmoveline(x, y, fx, fy):
                returnvalue = True
    return returnvalue

def domoveline(x,y,fx,fy):  # flips pieces in a line if possible
    global board
    loop = True
    if okmoveline(x, y, fx, fy):
        while loop:
            x += fx
            y += fy
            if 2 == inspace(x, y):
                board[y][x] = piece[turn]
            else:
                loop = False
def domove(x,y):    #puts down a piece from the current player and flips all pieces that should be flipped
    board[y][x] = piece[turn]
    for fx in range(-1,2):
        for fy in range(-1,2):
            domoveline(x, y, fx, fy)

board[4][4] = piece[0]  # creates the starting position in othello
board[3][3] = piece[0]
board[4][3] = piece[1]
board[3][4] = piece[1]
game = True
while game:
    print("   0 1 2 3 4 5 6 7 ")    
    for i in range(0,8):                    # prints the board one line at a time
        print(i,"|"+"|".join(board[i])+"|")
    Validmoveexists = False
    game = False
    for i in range(0,2): # resets points
        points[i] = 0
    for x in range(0,8):    
        for y in range(0,8):
            if 0 == inspace(x, y):  # checks if there are empty spaces
                if okmove(x,y):   # checks if the player can do a move that changes any opponent pieces
                    Validmoveexists = True
                game = True     
            for i in range(0, 2):   #counts points
                if board[y][x] == piece[i]:
                    points[i] += 1
    if game: 
        if Validmoveexists: 
            for i in range(0,2):
                print("Player",i+1,"",points[i],piece[i])
            movedone = False
            while not movedone:   # the current player puts down a piece
                print("Player",turn+1,)
                x = move("X")
                y = move("Y")
                if okmove(x, y):    #checks if the player can put a piece in the chosen position
                    domove(x, y)
                    movedone = True
                else:
                    print("That move doesn't flip any pieces")
        else:
            print("There is no valid move for player",turn+1,)
    if turn == 1:
        turn = 0
    else:
        turn = 1
if points[0] > points[1]:       # checks which player has won
    print("Player 1 won")
elif points[1] > points[0]:
    print("Player 2 won")
else:
    print("Draw")