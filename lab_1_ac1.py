def greet():
    # this function prints simple hello message
    print("Hello, World!")

greet()   # calling first greet function


def greet():
    # redefining function with new message
    print("Hello, Welcome to the Whitecliffe")

greet()   # calling updated greet function


def greet():
    # again same function but we will use it later
    print("Hello, Welcome to the Whitecliffe")


def numbers():
    # here we are taking two fixed numbers
    n1 = 15
    n2 = 70

    # doing addition
    result = n1 + n2

    # printing the result
    print("Sum of the numbers:", result)

# calling both functions
greet()    # this will call latest greet function
numbers()  # calling numbers function
