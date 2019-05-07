import os
import random


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


def print_snake(table):
    pass


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
            if move == "w":
                print("testing")
            elif move == "s":
                print("testing")
            elif move == "d":
                print("testing")
            elif move == "a":
                print("testing")


if __name__ == "__main__":
    main()
