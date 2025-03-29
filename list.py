'''a = ['apple', 'banana', 'mango', 'orange']
b = a
b.pop(1)
print(a) #pop method'''
'''a = [1, 2, 3]

# Add 4 to the end of the list
a.append(4)
print(a) # append'''

'''a = [1, 2, 3]

# Create a copy of the list
b = a.copy()
print(b) #copy'''

'''a = [1, 2, 3]

# Remove all elements from the list
a.clear()
print(a) # clear'''

'''a = [1, 2, 3, 2]

# Count occurrences of 2 in the list
print(a.count(2)) # count'''

'''a = [1, 2]

# Extend list a by adding elements from list [3, 4]
a.extend([3, 4])
print(a)'''

'''a = [1, 3]

# Insert 2 at index 1
a.insert(1, 2)
print(a) # insert'''

'''a = [1, 2, 3]

# Remove the first occurrence of 2
a.remove(2)
print(a) # remove'''

'''a = [1, 2, 3]

# Reverse the list order
a.reverse()
print(a) #reverse'''

'''a = [3, 1, 2]

# Sort the list in ascending order
a.sort()
print(a) #sort'''

print("welocome")
student = []
while 1:
    temp = []
    name = input("enter your name ")
    grades = input("enter your grades ")
    f=1
    for item in student:
        if name in item:
            print("name alredy exist add new name")
            f=0
    if f==0:
        continue
    else:
        temp.append(name)
        temp.append(grades)
        student.append(temp)
        n = input("if you want more tytpe y ")
        if n.lower() != 'y':
            break
print(student)










