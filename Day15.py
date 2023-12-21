print("-------Animal Sound Game-------")
exit = "no"
while exit != "yes":
    animal = input("What animal do you want?")
    if animal == "cow":
        print("A cow goes moo🐄🐮")
    elif animal == "bird":
        print("Oww it's too hard. Each bird species has its own unique vocalizations.🐦🐤")
    elif animal == "dog":
        print("A dog goe woof🐕‍🦺🐶")
    elif animal == "pig":
        print("The classic pig sound is often described as an 'oink'.🐖🐷")
    elif animal == "cat":
        print("A cat goes meow🐈🐱")
    elif animal == "rooster":
        print("The crowing is a series of loud and distinctive 'cock-a-doodle-doo' calls.🐓🐔")
    else:
        print("Oh I guess I couldn't find that animal's voice.")
    exit = input("\033[31mDo you want to exit?\033[0m")
