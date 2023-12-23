print("\033[36m---------------\033[0m")
print("\033[35mList Generator\033[0m")
print("\033[36m---------------\033[0m")
print("\033[34mI will ask you for starting, ending numbers and increasing amounts. and I will sort the numbers in between according to the amount of increase.\033[0m")
start = int(input("\033[37mStart at > \033[0m"))
end = int(input("\033[37mEnd before > \033[0m"))
inc = int(input("\033[37mIncrement between values > \033[0m"))
for i in range(start, end, inc):
  print(i)