count = 1   # starting value of count

def increment():
    global count   # using global so we can change it inside function

    # adding 3 to count each time function runs
    count += 3

    # showing updated value
    print(f"count inside the function: {count}")

# calling function multiple times
increment()   # first time
increment()   # second time
increment()   # third time

# printing final value outside function
print(f"count inside the function: {count}")


