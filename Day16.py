print("\033[34mFill-in the blank Lyrics!\033[0m")
print("-----------------------------------------")
print("\033[35mPlease guess the lyrics of the famous song and fill in the blank.\033[0m")
i = 0
while True:
    answer = input ("Oh I feel that it's real, Take my ______")
    if answer == "heart" or answer == "Heart":
        print("Well done, you got it.")
    else:
        print("Nope, try again.🥱")
    i += 1
    if answer == "heart":
        break
print("That's correct. You got it in",i , "attemps.🥳🥳")
