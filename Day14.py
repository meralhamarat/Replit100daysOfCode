from getpass import getpass as input

print("E P I C    🪨  📄 ✂️    B A T T L E ")
print()
print("Select your move (R, P or S)")
print()

firstPlayer = input("Player 1 > ")
secondPlayer = input("Player 2 > ")

if firstPlayer == "R":
  if secondPlayer == "R":
    print("You both picked Rock, draw!")
  elif secondPlayer == "P":
    print("Player1's Rock is smothered by Player2's Paper!")
  elif secondPlayer == "S":
    print("Player1 smashed Player2's Scissors into dust with their Rock!")
  else:
      print("Invalid Move Player 2!")
if firstPlayer == "P":
    if secondPlayer == "P":
        print("You both picked Paper, draw!")
    elif secondPlayer == "R":
        print("Player2's Rock is smothered by Player1's Paper!")
    elif secondPlayer == "S":
        print("Player1's Paper is cut into tiny pieces by Player2's Scissors!")
    else:
        print("Invalid Move Player 2!")
if firstPlayer == "S":
    if secondPlayer == "S":
        print("Ka-Shing! Scissors bounce off each other like a dodgy sword fight! Draw.")
    elif secondPlayer == "P":
        print("Player1's Scissors make confetti out of Player2's paper!")
    elif secondPlayer == "R":
        print("Player 2's Rock makes metal-dust out of Player1's Scissors")
    else:
        print("Invalid Move Player 2!")
else:
    print("Invalid Move Player 1!")
