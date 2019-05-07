def generate_table(column, row):
    table = []
    for i in range(column):
        table.append([0] * row)
    return table


def print_table(table):
    for row in table:
        one_row = ""
        for elem in row:
            one_row += str(elem)
        print(one_row)


def main():
    print_table(generate_table(20, 20))


if __name__ == "__main__":
    main()
