import random

print("---Welcome to NumFin Game---")
print("***********Rules************")
print("-You will try to find the number selected by the computer.")
print("-1 heart will decrease for every wrong answer.")
print("-Let's Start!!!")
print("Choose the difficulty level;")
print("Extreme => 1 heart")
print("Hard => 3 heart")
print("Medium => 6 heart")
print("Easy => 10 heart")

i = 0
while i == 0:
    difficulty = input("Press 'x' for extreme, press 'h' for hard, press 'm' for medium, press 'e' for easy: ").lower().lstrip().rstrip()
    if difficulty == "e":
        heart = 10
        i += 1
    elif difficulty == "m":
        heart = 6
        i += 1
    elif difficulty == "h":
        heart = 3
        i += 1
    elif difficulty == "x":
        heart = 1
        i += 1
    else:
        print("Plase press only 'x,h,m,e'.")

print("Enter value range.(Our recommendation is [0,100])")

a = 0
b = 0

while a == b:
    minValue = int(input("Enter a minimum value: "))
    maxValue = int(input("Enter a maximum value: "))
    if minValue < maxValue:
        print("ಠ_ಠ Let's see if you are a wizard ಠ_ಠ")
        a + 1
        break
    else:
        if minValue > maxValue:
            print("The minimum value cannot be greater than the maximum value.")
        elif minValue == maxValue:
            print("The minimum value cannot be equal to the maximum value.")

comnum = random.randint(minValue, maxValue)

while heart > 0:
    heart += -1
    pnum = int(input("Enter a number: "))

    if pnum == comnum:
        print(f"You Won. The number was {comnum}.")
        break
    elif comnum < pnum:
        print("Decrase the number.")
        if heart == 0:
            print(f"You lose. The number was {comnum}.")
        else:
            a = heart-1
            print(f"You have {a+1} heart left.")
    else:
        print("Incrase the number.")
        if heart == 0:
            print(f"You lose. The number was {comnum}.")
        else:
            a = heart-1
            print(f"You have {a+1} heart left.")

input("Press 'Enter' to exit the game.")