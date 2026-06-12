# Coursework Assessment 2
# Name: Javohir Tursunaliyev
# Student No:2427229
# noughts and crosses game
import random

def draw_board(board):
    for row in board:
        print("-" * 9)
        print(" | ".join(row))
        

def welcome(board):
    print("Welcome to Noughts and Crosses!")
    draw_board(board)

def initialise_board(board):
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '
            
def get_player_move(board):
    while True: 
        try:
            move = int(input("                      1 2 3  \n                      4 5 6 \nEnter the cell number 7 8 9 : "))
            if 1 <= move <= 9:
                row = (move - 1) // 3
                col = (move - 1) % 3
                if board[row][col] == ' ':
                    return row, col
                else:
                    print("Cell already occupied. Try again.")
            else:
                print("Invalid cell number. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def choose_computer_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(empty_cells)

def check_for_win(board, mark):
    for i in range(3):
        if all(board[i][j] == mark for j in range(3)):
            return True
    for j in range(3):
        if all(board[i][j] == mark for i in range(3)):
            return True
    if all(board[i][i] == mark for i in range(3)) or all(board[i][2 - i] == mark for i in range(3)):
        return True
    return False

def check_for_draw(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def play_game(board):
    initialise_board(board)
    welcome(board)
    player_mark = 'X'
    computer_mark = 'O'



    while True:
        row, col = get_player_move(board)
        board[row][col] = player_mark
        draw_board(board)
        if check_for_win(board, player_mark):
            print("Congratulations! You win!")
            return 1
        if check_for_draw(board):
            print("It's a draw!")
            return 0

        row, col = choose_computer_move(board)
        board[row][col] = computer_mark
        draw_board(board)
        if check_for_win(board, computer_mark):
            print("Computer wins!")
            return -1

def menu():
    while True:
        print("\nMenu:")
        print("1. Play Game")
        print("2. Display Leaderboard")
        print("3. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            board = [[' ' for _ in range(3)] for _ in range(3)]
            score = play_game(board)
            if score != 0:
                save_score(score)
        elif choice == '2':
            leaders = load_scores()
            display_leaderboard(leaders)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def load_scores():
    try:
        with open('leaderboard.txt', 'r') as file:
            leaders = {}
            for line in file:
                name, score = line.strip().split(',')
                leaders[name] = int(score)
            return leaders
    except FileNotFoundError:
        return {}

def save_score(score):
    try:
        name = input("Enter your name: ")
        with open('leaderboard.txt', 'a') as file:
            file.write(f"{name},{score}\n")
    except PermissionError:
        print("Error: Permission denied. Unable to save score.")

def display_leaderboard(leaders):
    print("\nLeaderboard:")
    if leaders:
        sorted_leaders = sorted(leaders.items(), key=lambda x: x[1], reverse=True)
        for i, (name, score) in enumerate(sorted_leaders, 1):
            print(f"{i}. {name}: {score}")
    else:
        print("Leaderboard is empty.")

if __name__ == "__main__":
    menu()