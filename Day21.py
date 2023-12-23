print("\033[34mWelcome To The Math Game!")
print("-------------------------\033[0m")
print("""In this game we gonna ask you some math questions, it's about multiplication table,
nd you have to answer them correctly! Let's get started!😊""")
print()
multiples = int(input("\033[36mEnter the multiple: \033[0m"))
counter = 0
for i in range(1, 11):
  solution = i * multiples
  answer = int(input(f"{i} x {multiples} ="))
  if answer == solution:
    print("Correct!")
    counter += 1
    print("Your score is", counter, "/10")
  else:
    print(f"Wrong! The correct answer is {solution}.")
    print("Your score is", counter, "/10")




