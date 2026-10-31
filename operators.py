#Operators are special symbols that perform an operation on values (called operands).

#----Arithmetic Operator == ("+" , "-" , "*" , "/" ,"//" , "%" , "**")
#----Compariosn Operator == ("==" , "!=" ,">", ">=", "<" , "<=")
#----Logical operator == ("and" , "or" , "not")


#----Arithmetic operator------#
a = 17
b = 5

print("Addition:", a + b)          # 22
print("Subtraction:", a - b)       # 12
print("Multiplication:", a * b)    # 85
print("Division:", a / b)          # 3.4
print("Floor division:", a // b)   # 3
print("Modulus:", a % b)           # 2
print("Power:", a ** 2)            # 289

#-----comparison operator------#
a = 17
b = 5

print(a == b)    # False
print(a != b)    # True
print(a > b)     # True
print(a < b)     # False
print(a >= 17)   # True
print(a <= 10)   # False

#----logical operator----------#
age = 20
marks = 70

print(age > 18 and marks > 60)    # True
print(age > 25 or marks > 60)     # True
print(not (age > 18))             # False