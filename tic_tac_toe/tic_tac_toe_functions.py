#display funcitons here

def create_board():
    my_board = []
    
    for i in range(3):
        my_board.append([])
        for j in range(3):
            my_board[i].append(" ")
    return my_board

#we add an extra 3 spaces at the start of all of these functions
#to help align the left indices

#this is the blank row above/below each entry in a square.
#makes it look nicer
def print_header():
    print(3*" "+3*" "+"|"+3*" "+"|"+3*" ")

#print a row
def print_row(row,row_index):
    print(f"{row_index}   {row[0]} | {row[1]} | {row[2]} ")

#print row separator
def print_row_sep():
    print("-  "+11*"-")

#display the board
def display_board(board):

    #prints our index
    print_row(["0","1","2"]," ")
    print("")
    
    for i in range(3):
        print_header()
        print_row(board[i],i)
        print_header()
        if (2 != i):
            print_row_sep()
        else:
            print("")


#our winning checks here

#check for a winning row
def check_row_winner(board):

    #bRowWinner = False
    
    for i in range(len(board)):
        if ((board[i][0] == board[i][1] ==board[i][2]) and " " != board[i][0]):
            return True

            
    return False

#check for a winning column
def check_column_winner(board):

    for i in range(len(board)):
        if ((board[0][i] == board[1][i] == board[2][i]) and " " != board[0][i]):
            return True
    return False

#check for a winning diagonal
def check_diagonal_winner(board):
    if ((board[0][0] == board[1][1] == board[2][2]) and " " != board[0][0]):
        return True
    if ((board[0][2] == board[1][1] == board[2][0]) and " " != board[0][2]):
        return True
    
    return False
    
#check for winning row, column, or diagonal
def check_winner(board):
    
    return check_row_winner(board) or check_column_winner(board) or check_diagonal_winner(board)


#check for a tie
def check_tie(board):
    return " " not in board[0] and " " not in board[1] and " " not in board[2]



#our user input selections


#get the user row selection
def get_row_selection():

    goodRows = ["0","1","2"]
    userRow = "BAD"

    while userRow not in goodRows:

        userRow = input("Please select a row (0,1,2): ")

        if userRow not in goodRows:
            print("Bad selection, try again.")
        else:
            print(f"You have selected row {userRow}")

    return int(userRow)

#get the user column selection
def get_column_selection():

    goodColumn = ["0","1","2"]
    userColumn = "BAD"

    while userColumn not in goodColumn:

        userColumn = input("Please select a column (0,1,2): ")

        if userColumn not in goodColumn:
            print("Bad selection, try again.")
        else:
            print(f"You have selected column {userColumn}")

    return int(userColumn)

#get the user selection of both row and column
def get_user_selection(board):

    goodChoice = False

    while not goodChoice:
        
        row = get_row_selection()
        column = get_column_selection()

        if (" " != board[row][column]):
            print("You picked a position already taken!")
        else:
            goodChoice = True

    print(f"You have selected row {row} and column {column}")
    
    return [row,column]


#symbol information here

#switch symbols between turns
def switch_symbol(symbol):

    if ("X" == symbol):
        return "O"
    if ("O" == symbol):
        return "X"

#ask player 1 which symbol they want
def get_first_player_symbol():

    p1Symbol = "BAD"

    while p1Symbol not in ["X","O"]:

        p1Symbol = input("Player 1, select symbol (X,O): ")

        if p1Symbol not in ["X","O"]:
            print("Bad symbol, try again!")
    
    return p1Symbol


#put the selection into the board
def update_board(selection,symbol,board):

    board[selection[0]][selection[1]] = symbol

    return board
    

#play the game function

def play_game():

    board = create_board()

    currentSymbol = get_first_player_symbol()
    
    
    #while no winner
    while not check_winner(board):
        display_board(board)

        #get selection and update board
        currentSelection = get_user_selection(board)
        board = update_board(currentSelection,currentSymbol,board)

        #check winner
        
        if check_winner(board):
            display_board(board)
            print(f"Yay, player {currentSymbol} won!")

        #if no winner, check for tie
        elif check_tie(board):
            display_board(board)
            print("No winner and no available spaces. Tie game!")
            
            break

        currentSymbol = switch_symbol(currentSymbol)
              

