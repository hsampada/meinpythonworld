## fib with fuction

def fib(a):
    if a<=1:
        return 1
    else:
        return fib(a-1)+fib(a-2)
fib(range(5))


#tabular format
print(tabulate([["sampada",30],["priyanka",20]],headers=["name","age"]))
