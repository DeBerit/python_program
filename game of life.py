x_length = 10
y_length = 10
infinity = False
optimization = False
board = []
living = "o"
dead = " "
generations = 100
generation = 0
def digits(number):
    if number < 10:
        return 1
    count = 1
    while True:
        if number < 10**count:
            return count
        count += 1

def int_input(maxvalue, prompt):
    while True:
        input_variable = input(prompt)
        if input_variable.isdigit():
            input_variable = int(input_variable)
            if input_variable <= maxvalue:
                return input_variable

def tilecount(x, y):
    if x >= 0 and x < x_length and y >= 0 and y < y_length:
        if board[x][y] == "living" or board[x][y] == "dying":
            return 1
        else:
            return 0
    else:
        return 0

def living_surrounding(x,y):
    count = 0
    count += tilecount(x + 1, y)
    count += tilecount(x + 1, y + 1)
    count += tilecount(x, y + 1)
    count += tilecount(x - 1, y)
    count += tilecount(x - 1, y - 1)
    count += tilecount(x, y - 1)
    count += tilecount(x + 1, y - 1)
    count += tilecount(x - 1, y + 1)
    

def print_board(space, num):
    for y in range(y_length):
        if num:
            string_num = str(y)
            print("{}{}".format(string_num," " * (digits(y_length)-digits(y))),end="")
        for x in range(y_length):
            if board[x][y] == "living":
                print(f"{space}{living}",end="")
            else:
                print(f"{space}{dead}",end="")
        print(space)

for i in range(x_length):
    board.append([])
    for n in range(y_length):
        board[i].append("dead")

while True:
    print_board("|",True)
    input_variable = input("Do you want to stop changing the state of tiles? y?")
    if input_variable != "y":
        input_variable = int_input(x_length,"X")
        input_variable2 = int_input(y_length,"Y")
        if board[input_variable][input_variable2] == "dead":
            board[input_variable][input_variable2] = "living"
        else:
            board[input_variable][input_variable2] = "dead"
    else:
        break
while True:
    print("generation:", generation)
    print_board(" ", False)
    for x in range(x_length):
        for y in range(y_length):
            if board[x][y] == "dead" and living_surrounding(x, y) == 3:
                board[x][y] = "birth"
            elif board[x][y] == "living":
                if living_surrounding(x, y) != 2 and living_surrounding(x, y) != 3:
                    board[x][y] = "dying"
    for x in range(x_length):
        for y in range(y_length):
            if board[x][y] == "dying":
                board[x][y] = "dead"    
            if board[x][y] == "birth":
                board[x][y] = "living"
    generation += 1
    if input("stop? y?") == "y":
        break