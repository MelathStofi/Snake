'''from pynput import keyboard  # Ehhez installálni kell a pip3-at "sudo apt install python3-pip" kommanddal, utána "pip3 install pynput" kommand.

# The currently active modifiers
current = set()


def on_press(key):
    pass


def on_release(key):
    pass


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


def execute():
    print("kakk")






import curses

# get the curses screen window
screen = curses.initscr()

# turn off input echoing
curses.noecho()

# respond to keys immediately (don't wait for enter)
curses.cbreak()

# map arrow keys to special values
screen.keypad(True)

try:
    while True:
        char = screen.getch()
        if char == ord('q'):
            break
        elif char == curses.KEY_RIGHT:
            # print doesn't work with curses, use addstr instead
            screen.addstr(0, 0, 'right')
        elif char == curses.KEY_LEFT:
            screen.addstr(0, 0, 'left ')
        elif char == curses.KEY_UP:
            screen.addstr(0, 0, 'up   ')
        elif char == curses.KEY_DOWN:
            screen.addstr(0, 0, 'down ')
finally:
    # shut down cleanly
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()





def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


while True:
    x = getch()
    if x == "w":
        print("testing")
    elif x == "s":
        print
'''




def menu():
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

if __name__ == "__main__":
    menu()