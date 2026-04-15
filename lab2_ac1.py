registration_counter = 50000   # starting value for registration id

def student_reg():
    global registration_counter   # using global so value can increase every time

    # assigning current id and then increasing for next student
    registration_id = registration_counter
    registration_counter = registration_counter + 1

    # taking all details from user
    date = input("Enter the registration date (DD/MM/YYYY): ")   # asking for date
    student_id = input("Enter the student ID: ")   # getting student id
    student_name = input("Enter the student name: ")   # getting name
    course_name = input("Enter your course name: ")   # asking course

    # sending all values back
    return date, student_id, student_name, course_name, registration_id


# calling the function and storing returned values
date, student_id, student_name, course_name, registration_id = student_reg()

# printing all the details
print("Printing student registration details:")
print(f"Date: {date}")   # showing date
print(f"Student ID: {student_id}")   # showing id
print(f"Student Name: {student_name}")   # showing name
print(f"Course Name: {course_name}")   # showing course
print(f"Registration Id: {registration_id}")   # showing reg id
