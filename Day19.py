print("\033[35mDebt Calculator\033[0m")
debt = 1000
apr = 0.05
for i in range(10):
    debt = (debt * apr) + debt
    print("Year", i+1, "is", round(debt, 2))