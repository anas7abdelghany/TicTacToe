import numpy as np
board= np.array([["", "", ""], ["", "", ""],["", "", ""]])


def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end="")
            if j < len(board[i]) - 1:
                print("|", end="")
        print("\n-----")
      
    
def get_move(board, player_symbol):
    while True:
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if board[row][col] == "":
                board[row][col] = player_symbol
                break
            else:
                print("That position is already taken!")
                
        except Exception as e:
            print(f"Invalid input : {str(e)}")

            
def check_win(board, player_symbol):
    for i in range(3):
        if all(board[i][j] == player_symbol for j in range(3)) or \
                all(board[j][i] == player_symbol for j in range(3)):
            return True
            
    if all(board[i][i] == player_symbol for i in range(3)) or \
            all(board[i][2 - i] == player_symbol for i in range(3)):
        return True
    
    return False


def check_tie(board):
    for row in board:
        if "" in row:
            return False  
    return True 


def tic_tac_toe():
    board = [["", "", ""] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    while True:
        print_board(board)
        player_symbol = players[current_player]
        get_move(board, player_symbol)

        if check_win(board, player_symbol):
            print_board(board)
            print(f"Player {player_symbol} wins!")
            break

        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        if current_player == 0:
            current_player = 1
        else:
            current_player = 0

tic_tac_toe()
