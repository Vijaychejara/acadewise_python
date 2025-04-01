def add_student(students):
    """Add a new student to the list if the name doesn't already exist."""
    while True:
        name_input = input("Enter your name: ")
        # Check if the name already exists in the list
        if any(student['name'] == name_input for student in students):
            print("Name already exists, try again.")
            continue
        
        grade_input = input("Enter your grade: ")
        # Create a student dictionary with name and grade
        student = {"name": name_input, "grade": grade_input}
        students.append(student)
        
        cont = input("Do you want to add another student? (y/n): ")
        if cont.lower() != 'y':
            break

def main():
    print("Welcome")
    students = []
    add_student(students)
    print("\nFinal Students List:")
    for student in students:
        print(f"Name: {student['name']}, Grade: {student['grade']}")

if __name__ == "__main__":
    main()
