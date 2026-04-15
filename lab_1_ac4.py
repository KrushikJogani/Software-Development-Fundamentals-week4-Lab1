def sum(a, b):
    # this function adds two numbers
    return a + b   # sending back addition


def multiply(x, y):
    # this function is for multiplication
    return x * y   # returning multiply result


def sum_and_multiply(a, b, c):
    # first we add a and b
    sumresult = sum(a, b)

    # then we multiply that result with c
    multiplyresult = multiply(sumresult, c)

    # giving final answer back
    return multiplyresult


# calling main function with values
result = sum_and_multiply(10, 20, 20)

# printing output
print(result)   # showing final result
