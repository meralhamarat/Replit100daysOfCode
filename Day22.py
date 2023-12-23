import random

answer = random.randint(1, 1000000)
print("Totally Random One-Million-To-One")

counter = 1
while True:
    guess = int(input("Guess the number > "))
    if answer > guess:
        print("Too low. Try again!")
        counter += 1
    elif answer < guess:
        print("Too high. Try again.")
        counter += 1
    elif answer == guess:
        print("That's correct!")
        break
    else:
        print("Invalid input. Try again.")
        exit()
print("It just took", counter, "guess")
