total = 0   # starting total value

def sum(num):
    global total   # using global so we can update total

    # adding given number into total
    total += num


def display():
    # printing the final total
    print(f"total sum: {total}")


# calling function with different values
sum(10)   # adding 10
sum(15)   # adding 15
sum(2)    # adding 2

# showing the result
display()
