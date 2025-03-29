print("welocome")
student = []
while 1:
    temp = {}
    name = input("enter your name ")
    grades = input("enter your grades ")
    f=1
    for item in student:
        if item['name']== name:
            print("name is alredy exist, try again")
            f=0
    if f==0:
        continue
    else:
        temp['name']=name
        temp['grades']=grades

        student.append(temp)
        n = input("if you want more tytpe y ")
        if n.lower() != 'y':
            break
print(student)