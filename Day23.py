print("R E P L I N - L O G I N - S Y S T E M")
def login():
    while True:
        username = input("Username > ")
        password = input("Password > ")
        if username == "meral" and password == "mfdol_21":
            print("Welcome to Replit Meral!")
            break
        else:
            print("Ops, try again!")
login()
