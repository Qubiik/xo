cletka = [" "] * 9
def map():
    print(cletka[0], '|', cletka[1], '|', cletka[2])
    print(cletka[3], '|', cletka[4], '|', cletka[5])
    print(cletka[6], '|', cletka[7], '|', cletka[8])
def player1():
    hot = int(input())
    match hot:
        case 1:
            cletka[0] = "X"
        case 2:
            cletka[1] = "X"
        case 3:
            cletka[2] = "X"
        case 4:
            cletka[3] = "X"
        case 5:
            cletka[4] = "X"
        case 6:
            cletka[5] = "X"
        case 7:
            cletka[6] = "X"
        case 8:
            cletka[7] = "X"
        case 9:
            cletka[8] = "X"
def player2():
    hot = int(input())
    match hot:
        case 1:
            cletka[0] = "O"
        case 2:
            cletka[1] = "O"
        case 3:
            cletka[2] = "O"
        case 4:
            cletka[3] = "O"
        case 5:
            cletka[4] = "O"
        case 6:
            cletka[5] = "O"
        case 7:
            cletka[6] = "O"
        case 8:
            cletka[7] = "O"
        case 9:
            cletka[8] = "0"
game = True
while game == True:
    map()
    player1()
    if cletka[0] == 'X' and cletka[1] == 'X' and cletka[2] == 'X':
        print("X winner!")
        game = False
    elif cletka[3] == 'X' and cletka[4] == 'X' and cletka[5] == 'X':
        print("X winner!")
        game = False
    elif cletka[6] == 'X' and cletka[7] == 'X' and cletka[8] == 'X':
        print("X winner!")
        game = False
    elif cletka[0] == 'X' and cletka[3] == 'X' and cletka[6] == 'X':
        print("X winner!")
        game = False
    elif cletka[1] == 'X' and cletka[4] == 'X' and cletka[7] == 'X':
        print("X winner!")
        game = False
    elif cletka[2] == 'X' and cletka[5] == 'X' and cletka[8] == 'X':
        print("X winner!")
        game = False
    elif cletka[0] == 'X' and cletka[4] == 'X' and cletka[8] == 'X':
        print("X winner!")
        game = False
    elif cletka[2] == 'X' and cletka[4] == 'X' and cletka[6] == 'X':
        print("X winner!")
    map()
    player2()
    if cletka[0] == 'O' and cletka[1] == 'O' and cletka[2] == 'O':
        print("O winner!")
        game = False
    elif cletka[3] == 'O' and cletka[4] == 'O' and cletka[5] == 'O':
        print("O winner!")
        game = False
    elif cletka[6] == 'O' and cletka[7] == 'O' and cletka[8] == 'O':
        print("O winner!")
        game = False
    elif cletka[0] == 'O' and cletka[3] == 'O' and cletka[6] == 'O':
        print("O winner!")
        game = False
    elif cletka[1] == 'O' and cletka[4] == 'O' and cletka[7] == 'O':
        print("O winner!")
        game = False
    elif cletka[2] == 'O' and cletka[5] == 'O' and cletka[8] == 'O':
        print("O winner!")
        game = False
    elif cletka[0] == 'O' and cletka[4] == 'O' and cletka[8] == 'O':
        print("O winner!")
        game = False
    elif cletka[2] == 'O' and cletka[4] == 'O' and cletka[6] == 'O':
        print("O winner!")
        game = False
