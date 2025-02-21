board = [" " for _ in range(9)]

def print_board():
    print("{} | {} | {}".format(board[0], board[1], board[2]))
    print("--+---+--")
    print("{} | {} | {}".format(board[3], board[4], board[5]))
    print("--+---+--")
    print("{} | {} | {}".format(board[6], board[7], board[8]))

def player_move(icon):
    if icon == "X":
        number = 1
    else:
        number = 2
    
    print("Your turn, player {}".format(number))
    while True:
        try:
            choice = int(input("Enter your move (1-9): ").strip())
            if 1 <= choice <= 9 and board[choice - 1] == " ":
                board[choice - 1] = icon
                break
            else:
                print("That space is taken or invalid! Try again.")
        except ValueError:
            print("Invalid input! Enter a number between 1 and 9.")

def is_victory(icon):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    return any(all(board[i] == icon for i in condition) for condition in win_conditions)

def is_draw():
    return " " not in board

while True:
    print_board()
    player_move("X")
    print_board()
    if is_victory("X"):
        print("X wins! Congratulations!")
        break
    if is_draw():
        print("It's a draw!")
        break
    
    player_move("O")
    print_board()
    if is_victory("O"):
        print("O wins! Congratulations!")
        break
    if is_draw():
        print("It's a draw!")
        break
