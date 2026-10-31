#CLASS 1 ----------- DATE = 28 SEPTEMBER---------------

# # # # Name = input("Enter your name :")
# # # # age = input("enter your age :")
# # # # result = name + " your age is " + str(age)
# # # # print( result)

# #//////////////2ND METHOD BY USNG F STRING////////
# # # college = "HLM"
# # # diploma = "nursing"
# # # year = 2023
# # # result = f"{college} is {diploma} college and the year is {year}"
# # # print (result)

# #//////////////3RD METHOD BY USING FORMAT METHOD////////////
# # school = "smvk"
# # classes = 12
# # result ="{} is upto {} standard.".format(school, classes)
# # print(result)

# #//////////////method 4 by using %operator/////////
# # name = "rahul"
# # age = 23
# # result = "%s is %d years old" % (name, age)
# # print(result)

# Name = "ayesha"
# age = 30 
# result = " %s is %d years old" % (Name, age)
# print(result)

# class 2------------date = 29september-------------

#/////////////multi-line comment////////////////
"""skdffsjd
srfjhfkwefj
fwjef
"""
#/////////////sum of two number where we have to take input/////////////

"""num1 = int(input("enter your num1 :"))
num2 = int(input("eneter your num2 :"))
multiply = num1 * num2
print("YOUR MULTIPLICATION IS :", multiply)"""

#/////////////find the area where we have to take input/////////////

"""side = float(input("enter the side :"))
area = side**2
print(area)"""

#-------------class - 3 date = 6/10-----------

# type casting  (in which change of data-type -------
# example : string to int,
"""x = "50"
print(x)    
print(type(x))

y = int(x)
print(y)
print(type(y))"""

# example : string to float 

"""price = "50.5"
price = float(price)
print(price)
print(type(price))"""

# using of list

"""friends = ["rawat","shoreya","anshu","soham"]
print(friends)
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])"""


"""friends = ["rawat","shoreya","anshu"]
friends.append("soham")
print(friends)"""

"""friends = ["rawat","shoreya","anshu","soham"]
friends.insert(1,"nidhi")
print(friends)"""

"""""friends = ["rawat","shoreya","anshu","soham"]
friends.insert(0,"prince")
print(friends)"""

"""even = [2,4,8,7,10]
even.append(6)
even.remove(7)
print(even)"""


#==================(date - 7/10)================--------

# print the element of list and also know what will show in -2 //////
"""students = ["amit" ,"soham" , "Prince" , "Anshu"]
print(students[0])
print(students[1])
print(students[2])
print(students[3])
print(students[-2])"""

#===============changing the element of a list===============# 

"""students = ["amit" ,"soham" , "Prince" , "Anshu"]

print ("before the change : " , students)

students[1] = "Shaurya"

print ("after the change : " , students)"""

#==============for print specific no of elements============#

"""students = ["Shaurya" ,"soham" , "Prince" , "Anshu"]

print("students are : " , students [:3])
print("students are : " , students [1:])
print("students are : " , students [1:])


print("total no of students are : " , len(students))"""

#=============for adding multiple no of element============#
"""games = ["BGMI" , "COD"]

new_games = ["GTA" , "FREE-FIRE"]

print ("Before extend : ", games)

games.extend(new_games)

print("after extend : " , games)"""

#===============for remove the item=========================#
"""games = ["BGMI" , "COD", "GTA" , "FREE-FIRE"]
print ("Before extend : ", games)
games.remove("FREE-FIRE")
print("after extend : " , games)"""

#===============DATE = (13/10)=========================#

#//////// FOR SWAPPING WITOUT 3RD VARIABLE//////////
""""a = float(input("enter first number = "))
b = float(input("enter second number = "))

a, b = b, a

print("swapped number a = " , a)
print("swapped number a = " , b)"""

#////////   for comparison variable  //////////

"""num1 = float(input("Enter Number 1 : "))
num2 = float(input("Enter Number 2 : "))

if num1 == num2 :
    print(True)

else :
      print (False)"""


"""age = 22
has_id = True

print(age >= 18 and has_id)
print(age < 18 and has_id)
print(not has_id)"""


"""language = ["Python" , "Java" , "C++"]

print("Python" in language)
print("ruby" in language)"""


"""language = "python"
cars = "BMW"

print(language.upper())
print(language.capitalize())
print(cars.lower())
"""

"""usertxt = "python_programming"
print(usertxt.strip())
print(usertxt.lstrip())
print(usertxt.rstrip())"""

#==================(date - 21/10)================--------

#///// for loop ///////#

"""for i in range(5):
    print("hello")"""


"""phone = ["iphone" , "Samsung" , "Redmi" , "Vivo","sssss","saas", "sdwfer"]
for e in phone[1 : 6 : 2]:
    print(e)"""

"""for i in range(1, 10 ,-1):
    print(i)"""


"""while  count >= 5:
    print(count)
    count -= count"""


#==================(date - 28/10)================--------

#checking the if& else condition 

"""raining = input("Is is raining ? (yes/no) :")

if(raining  == "yes"):
    print("You have to take umbrella")
else:
    print("You don't have to take umbrella")"""


"""Age= int(input("Enter your age :"))
if(Age >= 18):
    print("YOU ARE ELIGIBLE FOR VOITING")
else:
    print("YOU ARE NOT ELIGIBLE FOR VOITING")"""

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

"""Attendence = input("State that you have above 75% Attendance :")
Assignment = input("State that you have done assignment :")

if(Attendence >= "75" and Assignment == "yes"):
    print("Your are eligible for exam")
else:    
    print("Your are not eligible for exam")"""

"""ain = input("is it raining? (yes/no) ")
if rain== "yes":
    print("yes you have to take umberella")
else:
    print("no you don't have to take umberella")"""     
















