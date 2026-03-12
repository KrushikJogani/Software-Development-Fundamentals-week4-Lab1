registration_counter = 50000

def student_reg():
    global registration_counter

    registration_id = registration_counter
    registration_counter = registration_counter + 1

    date = input("Enter the registration dat(DD/MM/YYYY):")
    student_id = input("Enter the student ID :")
    student_name = input("enter the student name:")
    course_name = input("Enter your course name:")

    return date,student_id,student_name,course_name,registration_id

date,student_id,student_name,course_name,registration_id = student_reg()

print("Printing student registration details:")
print(f"Date:{date}")
print(f"Student ID:{student_id}")
print(f"Student Name:{student_name}")
print(f"Course Name:{course_name}")
print(f"Registration Id:{registration_id}")