# example for dictionaries #
"""students = {
    "name" : "Shaurya",
    "age" : 20,
    "roll_no" : 101,
    "course" : "BCA"       
}

print("Creating dictionary", students)
print("students name :", students["name"])
print("students age :", students["age"])
print("students roll_no :", students["roll_no"])
print("students course :", students["course"])

# example for dictionaries in which value are been taken by user #

std = {
    "name" : input("Enter your name :"),
    "age" : int(input("Enter your age :")),
    "roll_no" : int(input("Enter your roll_no :")),
    "course" : input("Enter your course :")
}
print("Creating dictionary", std)
#for adding new key or element in dctionaries 
std["city"] = "Delhi"
std["email"] = "amitg000022@gmail.com"
print(std)"""


"""biodata = {
    "name" : "nithya" ,
    "education" : "bca",
    "address" : "ghaziabad" ,
    "roll no" : 69 
}
print("creating dictionary :" , biodata)
print(biodata)

# keys() returns all keys.
print("Keys:", biodata.keys())
 
# values() returns all values.
print("Values:", biodata.values())
 
# items() returns keys and values.
print("Items:", biodata.items())"""


"""course = {
    "suject" : "BCA",
    "fees" : 40000,
    "duration" : 3
}
print("Toatl element :" , len(course))

if "subject" in course:
    print("Subject key is in dictionary")
else:
    print("subject key is not there")"""
print("\n12. nestesd dictionary")

students = {
    "student1" : {
        "name" : "Shaurya",
        "age" : 20,
        "roll_no" : 101,
        "course" : "BCA"
    },
    "student2" : {
        "name" : "Amit",
        "age" : 21,
        "roll_no" : 102,
        "course" : "BCA"
    },
    "student3" : {
        "name" : "Nithya",
        "age" : 22,
        "roll_no" : 103,
        "course" : "BCA","bcom","bba"
    }
}
print("Student 1 Name:", students["student1"]["name"])
print("Student 2 Name:", students["student2"]["name"])
print("Student 3 Name:", students["student3"]["name"])












