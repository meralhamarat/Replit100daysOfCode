print("\033[36m-----Guess The Number!------\033[0m")
print()
print("Hint = The number is between 1 and 100")
print()
counter = 0
answer = 85
while True:
    guess = int(input("What is your guess?:"))
    if guess > answer:
        print("Too high. Try again.")
        counter += 1
        continue
    elif guess < answer :
        print("Too low. Try again.")
        counter += 1
        continue
    elif guess == answer:
        print("Well done, you found the answer!")
        counter += 1
        break
    else:
        print("İnvalid input.")
        counter += 1
print("You found the number in just", counter, "guesses")