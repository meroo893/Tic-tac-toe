def is_free(pos):
    if board[pos] == " ":
        return True
    return False


def print_board():
    for i in range(1, 10):
        print(f"| {board[i]} ", end="")
        if i % 3 == 0:
            print("|")


def check_rows():
    for i in range(1, 8, 3):
        res = ""
        for j in range(3):
            res += board[i+j]
        if res == "XXX":
            return "X"
        elif res == "OOO":
            return "O"
    return None


def check_columns():
    for i in range(3):
        res = ""
        for j in range(1, 8, 3):
            res += board[i+j]
        if res == "XXX":
            return "X"
        elif res == "OOO":
            return "O"
    return None


def check_diagonals():
    main_d = ""
    sec_d = ""
    for i in range(1, 10, 4):
        main_d += board[i]
    for j in range(7, 2, -2):
        sec_d += board[j]
    if main_d == "XXX" or sec_d == "XXX":
        return "X"
    elif main_d == "OOO" or sec_d == "OOO":
        return "O"
    return None


def check_winner():
    if check_rows() is not None:
        return check_rows()
    if check_diagonals() is not None:
        return check_diagonals()
    if check_columns() is not None:
        return check_columns()


def call_by_symbol(sym):
    if sym == player_1[1]:
        return player_1[0]
    return player_2[0]


def choice_picker(player, choice):
    if is_free(choice):
        board[choice] = player[1]


def winner():
    winner_sym = check_winner()
    if winner_sym is not None:
        winner = call_by_symbol(winner_sym)
        return f"{winner} won!"
    return None


player_1 = ["", "X"]
player_2 = ["", "O"]

player_1[0] = input("Player one name: ")
player_2[0] = input("Player two name: ")

player_1[1] = input(f"{player_1[0]} would you like to play with 'X' or 'O'? ")
if player_1[1] == "X":
    player_2[1] = "O"

board = {}
print("This is the numeration of the board:")
for i in range(1, 10):
    print(f"| {i} ", end="")
    if i % 3 == 0:
        print("|")      # Moving to a new line
    board[i] = " "
print(f"{player_1} starts first!")

while True:
    p1_choice = int(input(f"{player_1} choose a free position [1-9]: "))
    choice_picker(player_1, p1_choice)
    print_board()
    win = winner()
    if win is not None:
        print(win)
        break

    p2_choice = int(input(f"{player_2} choose a free position [1-9]: "))
    choice_picker(player_2, p2_choice)
    print_board()
    win = winner()
    if win is not None:
        print(win)
        break