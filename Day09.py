rint("\033[34mGeneration-Finder-Inator\033[0m")
print("\033[32m***********************\033[0m")
year = int(input("What year were you born?"))
if year <= 1900:
    print("Waow Pasha, you are Lost Generation")
elif year >= 1901 and year <= 1927:
    print("That'S unbelieveble! You are the Greatest Generation")
elif year >= 1928 and year <= 1945:
    print("OMG, you are Silent Generation!")
elif year  >= 1946 and  year <= 1964:
    print("Hi BabyBoomer! You've seen it all and paved the way for the rest of us. Cheers to your wisdom!")
elif year >= 1965 and year <= 1981:
    print("What's up, Generation X!You guys rocked the '80s and '90s. Keep that rebellious spirit alive!")
elif year >= 1982 and year <= 1995:
    print("Hey yo Millennials, keep adulting like pros and turning avocado toast into a lifestyle.")
elif year >= 1996:
    print("Hey, Gen Z! TikTok much?")
else:
    print("Please try again.")
