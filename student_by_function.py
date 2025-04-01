def gretting():
    print("welcome")
student=[]
def add_input():
    while True:
        temp={}
        name = input("enter your name")
        grade = input("enter your grade")
        f=1
        for item in student:
            if item['name']== name:
                print("name is alredy exist, try again")
                f=0
        if f==0:
            continue
            
        temp['name']= name
        temp['grade']=grade
        student.append(temp)
        print(type(grade))
        return temp
        

def yes_no():
    n = input("if you want more tytpe y ")
    if n.lower() != 'y':
        return
    add_input()
    


add_input()
yes_no()
print(student)
        





    