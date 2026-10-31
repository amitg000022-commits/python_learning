"""A loop is a statement that repeats a block of code multiple times.
so you don’t have to write the same lines again and again"""

#----------------FOR LOOP---------#
for i in range(5):
    print("hello")

#===============loops in list======#
phone = ["iphone" , "Samsung" , "Redmi" , "Vivo","sssss","saas", "sdwfer"]
for e in phone[1 : 6]:
    print(e)

#   Table of 2   #
num = int(input("Enter a number for table :"))
for i in range(1,10):
    print(f"{num} x {i} = {num*i}")

#----------------While LOOP---------#
count = 1
while count <= 5:
    print(count)
    count += 1
