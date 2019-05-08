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


def generate_snake(table, move, column_index, row_index):
    pass


def generate_object(table):
    rand_col_index = random.randint(0, (len(table)-1))
    rand_row_index = random.randint(0, (len(table[rand_col_index])-1))
    table[rand_col_index][rand_row_index] = "Ó"


def main():
    board = generate_table(20, 30)
    column_index = 10
    row_index = 15
    while True:
        generate_object(board)
        print_table(board)

        while True:
            move = getch()
            generate_snake(board, move, column_index, row_index)
            if move == "w":
                column_index -= 1
            elif move == "s":
                column_index += 1
            elif move == "d":
                row_index += 1
            elif move == "a":
                row_index -= 1
            board[column_index][row_index] = "@"
            print_table(board)
            board[column_index][row_index] = " "


if __name__ == "__main__":
    main()
