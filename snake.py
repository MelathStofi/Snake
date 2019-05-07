def generate_table(column, row):
    table = []
    for i in range(column):
        table.append([" "] * row)
    return table


def print_table(table):
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


def main():
    print_table(generate_table(20, 30))


if __name__ == "__main__":
    main()
