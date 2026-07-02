#Tic tack toe game for two players

RED = "\033[31m"
BLUE = "\033[34m"
RESET = "\033[0m"

def intro():
    # This function introduces the rules of the game Tic Tac Toe
    print("\n")
    print("*************************** Tic Tac Toe ***************************")
    print("Rules: Player 1 and Player 2, represented by X and O, take turns "
          "marking the spaces in a 3*3 grid. \nThe player who succeeds in placing "
          "three of their marks in a horizontal, vertical, or diagonal row wins.")
    input("Press enter to continue.")
    print("\n")

def create_grid():
# This function creates a blank playboard
    print("Here is the playboard: ")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]        
    return board

def print_pretty(board):
# Display the current game board.
    rows = len(board)
    print("\n    0   1   2")
    print("  -------------")

    for r in range(rows):
        print(f"{r} | {board[r][0]} | {board[r][1]} | {board[r][2]} |")
        print("  -------------")
    return board

def sym():
    # This function decides the players' symbols
    while True:
        # Set the color of X to RED and O to BLUE
        symbol_1 = input("Player 1, do you want to be X or O? ").upper()
        if symbol_1 == "X":
            symbol_1 = RED + "X" + RESET
            symbol_2 = BLUE + "O" + RESET
            print("Player 2, you are O.")
            break
        elif symbol_1 == "O":
            symbol_1 = BLUE + "O" + RESET
            symbol_2 = RED + "X" + RESET
            print("Player 2, you are X.")
            break
        else:
            print("Invalid choice. Please enter X or O.")
            continue

    input("Press enter to continue.\n")

    # Set the color of X to RED and O to BLUE

    return(symbol_1, symbol_2)

def start_game(board, symbol_1, symbol_2, count):
    # This function starts the game.

    # Decides the turn
    player = symbol_1 if count % 2 == 0 else symbol_2

    print("Player "+ player + ", it is your turn. ")
    row, col = ask_cell(board)

    # Locates player's symbol on the board
    if player == symbol_1:
        board[row][col] = symbol_1  
    else:
        board[row][col] = symbol_2
    
    return (board)

def ask_cell(board):
    # This function asks the players for their choice of cell.
    while True:
        try:
            row = int(input("Pick a row (0-2): "))
            col = int(input("Pick a column (0-2): "))

            # Check if players' selection is out of range
            if row not in (0, 1, 2) or col not in (0, 1, 2):
                print("Coordinates must be between 0 and 2.")
                continue
            
            # Check if the square is already filled
            if board[row][col] != " ":
                print("That square is already occupied.")
                continue

            return row, col
        
        except ValueError:
            print("Please enter numbers only.")

def run_game(board, symbol_1, symbol_2):
    # This function runs the game until a player wins or the game ends in a tie.
    count = 0

    while count < 9:
        start_game(board, symbol_1, symbol_2, count)
        print_pretty(board)

        player = symbol_1 if count % 2 == 0 else symbol_2

        # Check if here is a winner
        if is_winner(board, player):
            print(f"\n🏆 Player {player} wins!\n")
            return player

        count += 1

    print("\n🤝 It's a tie!\n")
    print("Game over.")
    return None

def is_winner(board, player):
    # This function checks if any winner is winning
    
    # Check the rows
    for row in range (0, 3):
        if all(board[row][col] == player for col in range(3)):
            return True
   
    # Check the columns
    for col in range (0, 3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check the diagnoals
    if all(board[i][i] == player for i in range(3)):
        return True
    
    if all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False

def play_again():
    # This functions asks the players if they want to play again
    while True:
        choice = input("Do you want to play again? (Y/n): ").upper()
        if choice == "Y":
            return True
        elif choice == "N":
            return False
        else:
            print("Please enter Y or N.")
   
def main():
    # The main function
    try:
        intro()
        symbol_1, symbol_2 = sym()
        score_1 = 0
        score_2 = 0
        ties = 0

        while True:
            board = create_grid()
            print_pretty(board)
            winner = run_game(board, symbol_1, symbol_2)
            if winner == symbol_1:
                score_1 += 1
            elif winner == symbol_2:
                score_2 += 1
            else:
                ties += 1
            
            print("*********** SCOREBOARD ***********")
            print(f"Player {symbol_1}: {score_1}")
            print(f"Player {symbol_2}: {score_2}")
            print(f"Ties: {ties}")

            if not play_again():
                print("👋 Thanks for playing!")
                break
    except KeyboardInterrupt:
        print("\n\n👋 Game interrupted. Goodbye!")

# Call Main
if __name__ == "__main__":
    main()