print("Marvel Movie Character Creator")
print("--")
print()
print("Answer these questions and let's find out.")
print()
print("Please use 'yes' and 'no' for answer.")

spider = input("Do you like 'hanging around'?")
if spider == "no":
    print("Then you are not \033[31mSpider-man\033[0m")

iron = input("Do you like 'offensive' jokes?")
if iron == "no":
    print("Hmm, then you are not \033[32mIron-man\033[0m")

kong = input("Do you have a 'gravelly' voice?")
if kong == "no":
    print("Aww, then you are not \033[35mKong\033[0m")

captain = input("Do you often feel 'Marvelous'?")
if captain == "yes":
    print("Aha! You are \033[36mCaptain Marvel! Hi!\033[0m")

else:
    print(" Sorry, you are not a marvel charachter.")
