import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def computer_move(board):
    available_moves = [(row, col) for row in range(3) for col in range(3) if board[row][col] == ' ']
    return random.choice(available_moves)

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    print("Welcome to Tic Tac Toe!")

    while True:
        print_board(board)

        if current_player == 'X':
            row = int(input("Enter row number (0, 1, or 2): "))
            col = int(input("Enter column number (0, 1, or 2): "))
        else:
            print("Computer's turn...")
            row, col = computer_move(board)

        if board[row][col] != ' ':
            print("That cell is already taken. Try again.")
            continue

        board[row][col] = current_player

        winner = check_winner(board)
        if winner:
            print_board(board)
            if current_player == 'X':
                print("Player X wins!")
            else:
                print("Computer wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()