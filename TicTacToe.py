def display_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def is_board_full(board):
    for row in board:
        if '' in row:
            return False
    return True

def play_game():
    board = [['', '', ''], ['', '', ''], ['', '', '']]
    current_player = 'X'

    while True:
        display_board(board)
        while True:
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))
            if board[row][col] == '':
                board[row][col] = current_player
                break
            else:
                print("Invalid move. Try again.")
        if check_winner(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_board_full(board):
            display_board(board)
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

play_game()
