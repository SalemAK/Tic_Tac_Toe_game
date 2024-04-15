import random
print("welcome to Tec toc game")
print("#----------------------#")

position = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def board():
    print("\n+--------------+")
    print("|", end="")
    for x in range(len(position)):
        print(f" {position[x]} ", end=" |")
        if x == 2 or x == 5:
            print("\n+--------------+")
            print("|", end="")
    print("\n+--------------+")


def check(player, play):
    if position[player] == "X" or position[player] == "O":
        print("this position taken play again !")
        turn(play)
    else:
        position[player] = play


def turn(play):
    board()
    player = int(input(f"\nPlayer {play} pick a number ! "))
    if player < 0 or player > 8:
        print("invalid number, Try again")
        turn(play)
    else:
        check(player, play)


def winner(play):
    if position[0] == play and position[1] == play and position[2] == play:
        print(f"Player {play} win the game ")
        return True
    elif position[3] == play and position[4] == play and position[5] == play:
        print(f"Player {play} win the game ")
        return True
    elif position[6] == play and position[7] == play and position[8] == play:
        print(f"Player {play} win the game ")
        return True
    elif position[0] == play and position[3] == play and position[6] == play:
        print(f"Player {play} win the game ")
        return True
    elif position[1] == play and position[4] == play and position[7] == play:
        print(f"Player {play} win the game ")
        return True
    elif position[2] == play and position[5] == play and position[8] == play:
        print(f"Player {play} win the game ")
        return True
    elif position[0] == play and position[4] == play and position[8] == play:
        print(f"Player {play} win the game ")
        return True
    elif position[2] == play and position[4] == play and position[6] == play:
        print(f"Player {play} win the game ")
        return True


def bots(play):
    number = random.randint(0, 8)
    if position[number] == "X" or position[number] == "O":
        bots(play)
    else:
        position[number] = "O"


player_x = "X"
player_O = "O"
bot = "O"

bot_or_2players = input("You want to play vs (player/bot)? ").lower()
on = True
while on:
    if bot_or_2players == "bot":
        turn(player_x)

        if winner(player_x):
            board()
            on = False
        else:
            bots(bot)
            if winner(bots):
                board()
                on = False

    if bot_or_2players == "player":
        turn(player_x)
        if winner(player_x):
            board()
            on = False
        else:
            turn(player_O)

            if winner(player_O):
                board()
                on = False
