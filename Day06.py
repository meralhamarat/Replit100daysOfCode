print()
print("\033[33m+++++++++++++++\033[0m")
print("\033[31mMY LOGIN SYSTEM\033[0m")
print("\033[33m+++++++++++++++\033[0m")

username = input("Username > ")
password = input("Password > ")

if username == "David" and password == "totalyNotBald":
    print("\033[34mWhy hello there David, what a lovely accent you have,\033[0m")
    print("\033[34myou could have charmed your way in here even without a password\033[0m")
    print("\033[34mHave a great day.\033[0m")
    print("\033[34mDont't forget to wear a hat in the sun!\033[0m")
elif username == "Meral" and password == "Chaxds23-":
    print("\033[38mHi Meral! Waow  You look great, I like your outfit!\033[0m")
elif username == "Jack" and password == "J*cK_0341":
    print("\033[37mYo Jack, what's up, man?\033[0m")
else:
    print("Go away!")
