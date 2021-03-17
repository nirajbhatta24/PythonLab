#A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
#Ask user for their salary and year of service and print the net bonus amount.
salary=int(input("Enter a salary"))
YOS=int(input("Enter his years of service"))
if YOS>5:
    print("The bonus is",0.05*salary)
else:
    print("No bonus")