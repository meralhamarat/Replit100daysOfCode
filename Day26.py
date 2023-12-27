from replit import audio
import os, time

def play():
  print("Playing song...")
  source = audio.play_file('audio.wav')
  source.paused = False
  input("Press Enter to stop the song.")

while True:
  os.system('clear' if os.name == 'posix' else 'cls')
  print("\033[34m🎵 MyPOD Music Player\033[0m")
  time.sleep(1)
  print("\033[33mPress 1 to Play")
  time.sleep(1)
  print("Press 2 to Exit")
  time.sleep(1)
  print("Press anything else to see the menu again.")
  time.sleep(1)

  choice = input("Your choice: \033[0m")

  if choice == '1':
    play()
  elif choice == '2':
    print("Goodbye!")
    break
  else:
    continue
