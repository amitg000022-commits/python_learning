#list

friends = ["rawat","shoreya","anshu","soham"]
print("Elements of this list are :" , friends)
print("First element :" ,friends[0])
print("Second element :" ,friends[1])
print("Third element :" ,friends[2])
print("Fourth element :" ,friends[3])

# append() method is used to add an element in the end of the list
print("Before the append() method the list is :", friends) 
friends.append("nidhi")
print("After the append() method the list is :", friends)

#insert() method is used to add an element at a specific index in the list
print("Before the insert() method the list is :", friends)
friends.insert(1, "sakshi")
print("After the insert() method the list is :", friends)

#remove() method is used to remove an element from the list
print("Before the remove() method the list is :", friends)
friends.remove("anshu")
print("After the remove() method the list is :", friends)

#pop() method is used to remove an element from the list at a specific index
print("Before the pop() method the list is :", friends)
friends.pop(0)
print("After the pop() method the list is :", friends)

#slicing of list
print("Elements from index 1 to 3 :", friends[1:4])
print(friends[:5])

#extend 
new_li = ["pooja" , "anshu"]
friends.extend(new_li)
print(friends)