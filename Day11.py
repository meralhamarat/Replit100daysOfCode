print("\033[34mHow many seconds are in a year?\033[0m")
print("\033[36m***********************\033[0m")

leap = input("Is this a leap year?")
year = 365

if leap == "yes" or leap == "Yes":
    print((year + 1) * 24 * 60 * 60)
elif leap == "no" or leap == "No":
    print(year * 24 * 60 * 60)
else:
    print("Please use 'yes' or 'no'")