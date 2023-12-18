print("\033[32m$$$$$$$$$$$$$$$$$$$$$$$\033[0m")
print("Welcome to Tip Calculator")
print("\033[32m$$$$$$$$$$$$$$$$$$$$$$$\033[0m")

bill = float(input("How much did you spend?"))
tip = int(input("What percentage do you want do tip?"))
people = int(input("How many people in your groups?"))

bill_tip = tip / 100 * bill + bill
bill_each = bill_tip / people
final_owe = round(bill_each, 2)

print("Your owe is", final_owe)