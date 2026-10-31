#ways to print & take input in python#

#-------- ways to print inp pyhton--------#
name = "Amit"
roll_no = 1223
print("My name is ",name)
print("My roll number is ",roll_no)

#------Print using taking input -------#
name = input("Enter your name :")
roll_no = input("Enter your roll number :")
print("My name is ",name)
print("My roll number is ",roll_no)

#------ways to concetinate the string and variable------#

#--(1.) concetination using + operator----#
Name = input("Enter your name :")
age = input("enter your age :")
result = name + " your age is " + str(age)
print( result)

#--(2.) concetination using F strings----#
college = input("Enter your collegename :")
diploma = input("Enter your diploma coursename :")
year = input("Enter your current year :")
result = f"Your college is {college} and diploma is {diploma} and the year is {year}"
print (result)

#--(3.) concetination using .format----#
school = input("Enter your school name :")
classes = input("Enter your class :")
result ="{} is upto {} standard.".format(school, classes)
print(result)

#--(4.) concetination using % operator----#
name = input("Enter your name :")
age = input("Enter your age :")
result = "%s is %d years old" % (name, int(age))
print(result)
