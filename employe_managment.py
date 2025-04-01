class Employee:
    def __init__(self, ):
        self.name = input("enter employe name")
        self.id = input("enter emplye id")
        self.salary = float(input("enter emplye salary"))
        self.department = input("enter your department")
        self.hours_worked = int(input("enter houres"))

    def calculate_salary(self):
        overtime = 0
        if self.hours_worked > 50:
            overtime = self.hours_worked - 50
        self.salary = self.salary + (overtime * (self.salary / 50))
        

    

    def print_employee_details(self):
        print("\nName: ", self.name)
        print("ID: ", self.id)
        print("Salary: ", self.salary)
        print("Department: ", self.department)
        print("----------------------")


employee1 = Employee()
print("Original Employee Details:")
employee1.calculate_salary()

employee1.print_employee_details()



