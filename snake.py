import os
import random
import sys
import tty
import termios


def generate_menu():
    # menu generator for snake 
    print("************Welcome to Snake**************")
    print()

    choice = input("""
                      A: Start Game
                      B: Highscore
                      Q: Quit

                      Please enter your choice: """)

    if choice == "A" or choice == "a":
        start_game()
    elif choice == "B" or choice == "b":
        highscore()
    elif choice == "Q" or choice == "q":
        sys.exit
    else:
        print("You must only select either A or B")
        print("Please try again")
        menu()


def start_game():
    pass


def highscore():
    pass


def getch():
    # Ez itt a billentyűzetfigyelő függvény!
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def generate_table(column, row):
    table = []
    for i in range(column):
        table.append([" "] * row)
    return table


def print_table(table):
    os.system("clear")
    dash = "--"
    for row in table:
        for elem in row:
            dash += "-"
        break

    print(dash)
    for row in table:
        one_row = ""
        for elem in row:
            one_row += str(elem)
        print(f"|{one_row}|")
    print(dash)


def generate_snake(table, move, column_index, row_index):
    pass


def generate_object(table, obj):
    rand_col_index = random.randint(0, (len(table)-1))
    rand_row_index = random.randint(0, (len(table[rand_col_index])-1))
    table[rand_col_index][rand_row_index] = obj


def find_object(table, obj):
    place = []
    for i_zero, row in enumerate(table):
        for i_one, elem in enumerate(row):
            if elem == obj:
                place.extend([i_zero, i_one])
                break
    return place


def print_score(score):
    print(f"score: {score}\n")


def main():
    board = generate_table(20, 30)
    object_char = "Ó"
    coordinates = [10, 15]
    score = 0
    while True:
        board[coordinates[0]][coordinates[1]] = "@"
        generate_object(board, object_char)
        object_place = find_object(board, object_char)
        print_table(board)
        print_score(score)
        while True:
            try:
                board[coordinates[0]][coordinates[1]] = " "
                if coordinates == object_place:
                    score += 1
                    break

                else:
                    move = getch()
                    # generate_snake(board, move, column_index, row_index)
                    if move == "w":
                        coordinates[0] -= 1
                    elif move == "s":
                        coordinates[0] += 1
                    elif move == "d":
                        coordinates[1] += 1
                    elif move == "a":
                        coordinates[1] -= 1
                    board[coordinates[0]][coordinates[1]] = "@"
                    print_table(board)
                    print_score(score)
            except:
                print("GAME OVER")

                sys.exit()


if __name__ == "__main__":
    main()
