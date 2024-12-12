board = ["-","-","-","-","-","-","-","-","-"]

# The board to play game on
def display_board():
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " | ")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " | ")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " | ")

  # the_game_is_on shows the game is not over yet
the_game_is_on = True 
# winner is get updated when game ends
Winner = None
# current player is player whose turn is play the game
current_player = "X"

# The function to handle gaming operations
def play_game():
    global current_player
    display_board()
    while the_game_is_on:
      handle_turn(current_player)
      check_if_game_is_over()
      flip_player()
    if Winner == "X" or Winner == "O":
        print(Winner + " Won")
    else:
        print("Tie")

def handle_turn(current_player):
    print(current_player + "'s turn ")
    position = input("Enter your position: \n")
    if position not in ["1","2","3","4","5","6","7","8","9"]:
        print("Invalid input")
        position = input("Enter your position: \n")
    position =int(position) - 1
    board[position] = current_player
    display_board()

def check_if_game_is_over():
    check_for_win()
    check_if_tie()

def check_for_win():
    global Winner
    row_winner = check_rows()
    column_winner = check_col()
    diagonal_winner =  check_diagonal()
    if row_winner:
       Winner = row_winner
    elif column_winner:
       Winner = column_winner
    elif diagonal_winner:
       Winner = diagonal_winner
    return

def check_rows():
    global the_game_is_on
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        the_game_is_on = False
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]
    return
def check_col():
    global the_game_is_on
    col_1 = board[0] == board[3] == board[6] !="-"
    col_2 = board[1] == board[4] == board[7] !="-"
    col_3 = board[2] == board[5] == board[8] !="-"
    if col_1 or col_2 or col_3:
        the_game_is_on = False
    if col_1:
        return board[0]
    if col_2:
        return board[1]
    if col_3:
        return board[2]
    return
def check_diagonal():
    global the_game_is_on       
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    if diagonal_1 or diagonal_2 :
        the_game_is_on = False
    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[2]
    return
def check_if_tie():
    global the_game_is_on
    if "-" not in board:
        the_game_is_on = False
    return

def flip_player():
    global current_player, player_2, player_1
    if current_player == "X":
        print("Its + str{player_2}+'s turn")
        current_player = "O"
    elif current_player == "O":
        print("Its + str{player_1}+'s turn")
        current_player = "X"
    return

play_game()