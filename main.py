import random

print("***** WELCOME TO SNAKE & LADDERS GAME *****")
print("-------------------------------------------")
snakes = {94: 24, 60: 42, 21: 4, 85: 16}
ladders = {5: 25, 44: 70, 80: 95, 12: 56}
pos = [0, 0]
i = 0
c = 0
while pos[0] < 100 and pos[1] < 100:
    input("Player " + str(i) + " turn")
    dice_num = random.randint(1, 6)
    c += 1
    pos[i] = pos[i] + dice_num
    if pos[i] < 100:
        print("you are at " + str(pos[i]))
        if pos[i] in snakes:
            pos[i] = snakes[pos[i]]
            print("Oops! you are encountered with snake and moving to " + str(pos[i]))
        elif pos[i] in ladders:
            pos[i] = ladders[pos[i]]
            print("Kudos! Its a ladder and bouncing to " + str(pos[i]))
    elif pos[i] > 100:
        print("Its " + str(dice_num) + " Try Again")
        pos[i] = pos[i] - dice_num
    i = (i + 1) % 2
    print("---------------------------")
if pos[0] == 100:
    print("\n Felicitations!!! player 0 rocked the game and remained as a winner..")
elif pos[1] == 100:
    print("\n Felicitations!!! player 1 rocked the game and remained as a winner..")