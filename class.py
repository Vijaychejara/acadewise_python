class student:
    def __init__(self,students=[]):
        self.students = students

    def greeting_message(self):
        print("welcome")

    def add_input(self):
        name = input("enter your name")
        grade= input("enter your grade")
        return name,grade
        
    def check_student_already(self,name):
        for student in self.students:
            if student['name']== name:
                print("name is alredy exist")
                return True
            return False
    
    def loops(self):
        while True:
            temp={}
            name,grade = self.add_input()
            if self.check_student_already(name):
                print("name is already exist")
                continue
            else:
                temp['name'] = name
                temp['grades']= grade
                self.students.append(temp)
                print("student added succesfully")
                print("do you want to add another ,type y")
                choice = input()
                if choice.lower()!='y':
                    break
            print("thank you")
    def __str__(self):
        return str(self.students)
p1 = student()
print(p1.greeting_message())


print(p1.loops())
