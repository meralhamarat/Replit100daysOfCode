print("\033[34mExam Grade Calculator\033[0m")
name = input("Name of the exam > ")
print()
maxScore = int(input("Maximum score is > "))
print()
yourScore = int(input("Your score is > "))
percentScore = float(yourScore / maxScore) * 100
round(percentScore, 2)

if percentScore <= 100 and percentScore >= 90:
    print("Congratulations on achieving an", round(percentScore,2), "in the", name,"which is an A+🥳" )
elif percentScore <= 89 and percentScore >= 80:
    print("Waow, that's awesome you got", round(percentScore,2), "in the", name, "which is an A- 🤓")
elif percentScore <= 79 and  percentScore >= 70:
    print("You got", round(percentScore,2), "in the", name, "which is a B 💪")
elif percentScore <= 69 and  percentScore >= 60:
    print("You got", round(percentScore,2), "in the", name, "which is a C 🫡")
elif percentScore <= 59 and percentScore >= 50:
    print("You got", round(percentScore, 2), "in the", name, "which is a D 😬")
if percentScore <= 49 and percentScore >= 40:
    print("You got", round(percentScore, 2), "in the", name, "which is a U 😖")
else:
    print("Dude, you should work hard😵💀☠️")