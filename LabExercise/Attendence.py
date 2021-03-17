#A student will not be allowed to sit in exam if his/her attendence is less than 75%.
#Take following input from user
#Number of classes held
#Number of classes attended.
#And print
#percentage of class attended
#Is student is allowed to sit in exam or not.
classes_held=int(input("Enter the number of classes held"))
classes_attended=int(input("Enter the number of classes attended"))
attendence=float(classes_attended/classes_held)*100

if attendence>=75:
    print("you are allowed to sit in exam")
else:
    print("you are not allowed")