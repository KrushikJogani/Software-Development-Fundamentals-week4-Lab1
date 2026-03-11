def sum(a,b):
    return a + b
def multiply(x,y):
    return x*y
def sum_and_multiply(a,b,c):
    sumresult = sum(a,b)
    multiplyresult = multiply(sumresult,c)
    return multiplyresult

result = sum_and_multiply(10,20,20)
print(result) 