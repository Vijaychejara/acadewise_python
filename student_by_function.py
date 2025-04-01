print("welocome")
student = []
def name():
    while 1:
        temp = {}
        name = input("enter your name ")
    
        f=1
        for item in student:
            if item['name']== name:
                print("name is alredy exist, try again")
            f=0
        if f==0:
            continue
        else:
            temp['name']=name
            student.append(temp)
            n = input("if you want more tytpe y ")
            if n.lower() != 'y':
                break
        print(student)
def grades():
    tem = {}
    grade = input("enter your grades")
    tem['grade']=grades
    student.append(tem)
    print(grade)
 
name()
grades()