
#A school has following rules for grading system:
#a. Below 25 - F
#b. 25 to 45 - E
#c. 45 to 50 - D
#d. 50 to 60 - C
#e. 60 to 80 - B
#f. Above 80 - A
#Ask user to enter marks and print the corresponding grade.
marks=int(input("Enter a marks"))
if marks<25:
    print("You have secured F grade")
elif marks>=25 and marks<45:
    print("You have secured E grade")
elif marks>=45 and marks<50:
    print("You have secured D grade")
elif marks>=50 and marks<60:
    print("You have secured C grade")
elif marks>=60 and marks<80:
    print("You have secured B grade")
else:
    print("You have secured A grade")
