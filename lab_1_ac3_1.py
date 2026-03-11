total = 0
def sum(num):
    global total
    total += num
def display():
    print(f"total sum: {total}")

sum(10)
sum(15)
sum(2)
display()