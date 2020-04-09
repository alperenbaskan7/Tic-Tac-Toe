import itertools
from colorama import Fore,Back,Style,init
init()
def win(current_game):
    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    for row in game:
        #print(row)
        if all_same(row):
            print(f"Player {row[0]} is the Winner,horizontally!")
            return True

        diag = []
        for col, row in enumerate(reversed(range(len(game)))):
            diag.append(game[row][col])
        if all_same(diag):
            print(f"Player {diag[0]} is the winner diagonally(/)!")
            return True

    diag = []

    for ix in range(len(game)):
        diag.append(game[ix][ix])
        #print(diag)
    if all_same(diag):
        print(f"Player {diag[0]} is the Winner,diagonally  (\\)!")
        return True

    for col in range(len(game)):  # it is like a basic for loop starts counting 0 to 3
        check = []  # it is for assigning column elements and check if they are the same.
        for row in game:  # adds row elements to check one by one
            check.append(row[col])  # adds first elements of row to check list.after second and third
        if all_same(check) : # controls if check has same elements to decide if game is won
            print(f"Player {check[0]} is the winner verticially!")
            return True
    return False


def game_board(game_map,player=0, row=0,column=0, just_display=False):
    try:# program will try using the function assignments, if user enters invalid input , program shows error message by except7
        if game_map[row][column] != 0:
            print("This position is occupado! Choose another!")
            return game_map,False
        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        if not just_display: #enters this conditions when user inputs
            game_map[row][column] = player #the move by the user
        for count , row in enumerate(game_map):
            colored_row =""
            for item in row:
                if item ==0:
                    colored_row += "  "
                elif item ==1 :
                    colored_row += Fore.GREEN + ' X ' + Style.RESET_ALL
                elif item ==2 :
                    colored_row += Fore.MAGENTA + ' O ' + Style.RESET_ALL
            print(count,colored_row)


        return game_map,True

    except IndexError as e: #invalid user input condition
        print("Error: make sure that you entered 0,1 or 2",e)
        return game_map,False
    except Exception as e:
        print("Something went really wrong!",e)
        return game_map,False
play= True
players = [1,2]
while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            ]
    game_won = False
    game, _ = game_board(game,just_display=True)
    player_choice = itertools.cycle([1,2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Current player:{current_player}")
        played = False

        while not played:
            column_choice = int(input("What column do you want to play? (0,1,2):"))
            row_choice = int(input("What row do you want to play? (0,1,2):"))
            game,played = game_board(game,current_player,row_choice,column_choice)
        if win(game):
            game_won = True
            again = input("The game is over would you like to play again? (y/n)")
            if again.lower() == "y":
                print("restarting")
            elif again.lower() == "n":
                print("Bye then")
                play = False
            else :
                print("Invalid answer see you later")
                play = False




