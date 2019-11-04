"""
7. (Game: play a tic-tac-toe game)
In a game of tic-tac-toe, two players take turns marking an available cell
in a grid with their respective tokens (either X or O).
When one player has placed three tokens in a horizontal, vertical, or diagonal
row on the grid, the game is over and that player has won. A draw (no winner)
occurs when all the cells in the grid have been filled with tokens and neither player
has achieved a win. Create a program for playing tic-tac-toe.
The program prompts two players to alternately enter an X token and an O
token. Whenever a token is entered, the program redisplays the board on the
console and determines the status of the game (win, draw, or continue).
"""

## This program is a tic-tac-toe game

# Define player constants
P1 = "X"
P2 = "O"

## Define variables

# set players into tuple since they will not change
tuple_players = ("Player 1", "Player 2")

# set available choices as list due to the
# choices being removed as they are chosen
list_available_choices = ["tl", "tm", "tr", "cl", "cm", "cr", "bl", "bm", "br"]
list_top_row = ["_", "_", "_"]
list_center_row = ["_", "_", "_"]
list_bottom_row = ["_", "_", "_"]

# function that prints the current state of the game board
# the top row, center row, and bottom row lists must be passed in as arguments
def print_game(t_row, c_row, b_row):
    game_board_list = [t_row, c_row, b_row]
    game_title = "    TIC-TAC-TOE    "
    game_board_top = " _________________"
    game_board_separator = "|     |     |     |"
    game_board_bottom = "|_____|_____|_____|"
    print(game_title)
    print(game_board_top)
    for row in game_board_list:
        print(game_board_separator)
        print(f"|  {row[0]}  |  {row[1]}  |  {row[2]}  |")
    print(game_board_bottom + "\n")

print_game(list_top_row, list_center_row, list_bottom_row)
print(len(list_available_choices))

# check length of list_available_choices
while len(list_available_choices) > 0:
    # foreach player in tuple_players
    for player in tuple_players:
        # set player input to nothing to begin loop
        player_input = ""
        
        # loop until player inputs one of the choices in list_available_choices
        # using try except just in case the lower() happens to develop an error
        while player_input not in list_available_choices:
            try:
                for choice in list_available_choices:
                    print(choice + " ",end='')
                print()
                player_input = input(player + ", choose one of the above locations: ")
                print("player input is: ", player_input)
                #player_input = input(", choose one of the following locations:")
                list_available_choices = 0
            except:
                print('Im in the except.')
                continue
        # remove the player's choice from the list of available choices
        list_available_choices.remove(player_input)

        # set mark to match the mark of the current player
        if player == "Player 1":
            mark = P1
        else:
            mark = P2

        # set the player's specific mark ('X' or 'O') in the appropriate location based on player_input
        if player_input == "tl": # if player input is top left
            list_top_row[0] = mark
        elif player_input == "tm": # if player input is top middle
            list_top_row[1] = mark
        elif player_input == "tr": # if player input is top right
            list_top_row[2] = mark
        elif player_input == "cl": # if player input is center left
            list_center_row[0] = mark
        elif player_input == "cm": # if player input is center middle
            list_center_row[1] = mark
        elif player_input == "cr": # if player input is center right
            list_center_row[2] = mark
        elif player_input == "bl": # if player input is bottom left
            list_bottom_row[0] = mark
        elif player_input == "bm": # if player input is bottom middle
            list_bottom_row[1] = mark
        else: # if player input is bottom right
            list_bottom_row[2] = mark

        # print the game board to show current status of game and available options
        print_game(list_top_row, list_center_row, list_bottom_row)
    
# check for who one the game

# if player one has all in one of the rows
if (all(P1 for elem in list_top_row) or 
    all(P1 for elem in list_center_row) or 
    all(P1 for elem in list_bottom_row) or 

# if player one has one in top left, one in center middle, and one in bottom right
    list_top_row[0] == P1 and list_center_row[1] == P1 and list_bottom_row[2] == P1 or 

# if player one has one in top left, one in center left, and one in bottom left
    list_top_row[0] == P1 and list_center_row[0] == P1 and list_bottom_row[0] == P1 or 

# if player one has one in top middle, one in center middle, and one in bottom middle
    list_top_row[1] == P1 and list_center_row[1] == P1 and list_bottom_row[1] == P1 or 

# if player one has one in top right, one in center right, and one in bottom right
    list_top_row[2] == P1 and list_center_row[2] == P1 and list_bottom_row[2] == P1 or 

# if player one has one in top right, one in center middle, and one in bottom left
    list_top_row[2] == P1 and list_center_row[1] == P1 and list_bottom_row[0] == P1):
        print("Player 1 wins!")

# if player one has all in one of the rows
elif (all(P2 for elem in list_top_row) or 
    all(P2 for elem in list_center_row) or 
    all(P2 for elem in list_bottom_row) or

# if player one has one in top left, one in center middle, and one in bottom right
    list_top_row[0] == P2 and list_center_row[1] == P2 and list_bottom_row[2] == P2 or

# if player one has one in top left, one in center left, and one in bottom left
    list_top_row[0] == P2 and list_center_row[0] == P2 and list_bottom_row[0] == P2 or

# if player one has one in top middle, one in center middle, and one in bottom middle
    list_top_row[1] == P2 and list_center_row[1] == P2 and list_bottom_row[1] == P2 or

# if player one has one in top right, one in center right, and one in bottom right
    list_top_row[2] == P2 and list_center_row[2] == P2 and list_bottom_row[2] == P2 or

# if player one has one in top right, one in center middle, and one in bottom left
    list_top_row[2] == P2 and list_center_row[1] == P2 and list_bottom_row[0] == P2):
        print("Player 2 wins!")