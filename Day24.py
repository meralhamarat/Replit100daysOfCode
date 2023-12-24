import random
print("🎲 Infinity Dice 🎲")
def rollDice(sides):
    number = random.randint(1, sides)
    print("You rolled", number)
while True:
    a = int(input("How many sides?"))
    rollDice(a)
    leave = input("Rolled again? ")
    if leave == "yes" or leave == "Yes":
        rollDice(a)
    else:
        exit()