#A conditional statement is a statement that makes a decision.
#It checks a condition, and the program runs a block of code only if that condition is true.

#----------------simple if condition------------#
#WAP to verify is child is adult or not
age = int(input("Enter your current age : "))
if age >= 18:
    print("Adult")

#----------------if-else condition--------------#
#WAP to verify is child is adult or minor
if age >= 18:
    print("Adult")
else:
    print("Minor")


#----------------if-elif-else condition----------#
#WAP to verify is raining or not
raining = input("Is is raining ? (yes/no) :")
if(raining  == "yes"):
    print("You have to take umbrella")
elif(raining == "no"):
    print("You don't have to take umbrella")
else:
    print("Take your own risk")

#WAP to verify the student grades with and operator
marks = int(input("Enetr your marks :"))
if(marks >= 90):
    print("A+")
elif(marks >= 80 and marks < 90):
    print("A")
elif(marks >= 70  and marks < 80):
    print("B")
elif(marks >= 60 and marks < 70):
    print("C")
else:
    print("Fail")

#WAP to verify is student is eligible for exam or not by assignment and attendence
Atten = int(input("State that you have above 75% Attendance :"))
Assign = input("State that you have done assignment :")

if(Atten >= 75 and Assign == "yes"):
    print("Your are eligible for exam")
elif(Atten >= 75 and Assign == "no"):
    print("Your Assignment is not submitted yet") 
elif(Atten <= 70 and Assign == "no"):
    print("Your Attendence is not above or equal to the 75% ")    
else:    
    print("Your are not eligible for exam")

#----------------nested condition----------#
#WAP to check the user password entered is right or not by nested 
username = "amit"
password = "1234"

if username == "amit":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("User not found")






