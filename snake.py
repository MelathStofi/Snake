import os
import random
import time


def getch():
    # Ez itt a billentyűzetfigyelő függvény!
    import sys, tty, termios
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


def generate_snake(table, move):
    col_ind = 10
    row_ind = 15

    if move == "w":
        col_ind -= 1
    elif move == "s":
        col_ind += 1
    elif move == "d":
        row_ind += 1
    elif move == "a":
        row_ind -= 1
    table[col_ind][row_ind] = "@"


def generate_object(table):
    rand_col_index = random.randint(0, (len(table)-1))
    rand_row_index = random.randint(0, (len(table[rand_col_index])-1))
    table[rand_col_index][rand_row_index] = "Ó"


def main():
    board = generate_table(20, 30)

    while True:
        generate_object(board)
        print_table(board)

        while True:
            move = getch()
            generate_snake(board, move)
            time.sleep
            os.system("clear")
            print_table(board)


if __name__ == "__main__":
    main()
