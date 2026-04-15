def greet(name):
    # this function is used to greet the person
    print(f"Good Morning {name}")   # showing message on screen

# calling function for different users
greet("krushik")   # for first name
greet("amritpal")  # for second name


def numbers(a, b):
    # here we are just adding two numbers
    return a + b   # giving back the result

# storing answers in variables
result_1 = numbers(10, 20)   # adding two integers
result_2 = numbers(0.2, 1)   # adding decimal and number

# printing results
print(result_1)   # print first answer
print(result_2)   # print second answer
