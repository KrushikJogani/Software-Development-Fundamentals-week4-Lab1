count = 1
def increment():
    global count
    count += 3
    print(f"count inside the function: {count}")

increment()
increment()
increment()

print(f"count inside the function: {count}")



