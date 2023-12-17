print("""
Welcome to your adventure simulator! 
I'm going to ask you a bunch of questions and then create an epic story with you as the star!""")

name = input("What is your name?")
enemy = input("What is your worst enemy's name?")
superpower = input("What is your superpower?")
live = input("Where do you live?")
food = input("What is your favorite food?")

print("Hello\033[35m", name, "\033[0m! Your ability to", superpower, "will make sure you never have to look at\033[31m", enemy, "\033[0magain. Go eat"
      , food, "as you walk down the streets of\033[34m", live, "\033[0mand use", superpower, "for good and not evil!")
