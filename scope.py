##x=2
##def local():
##    x=3
##    print(x)
##local()
##print(x)
##
##
##x=4
##def local1():
##    global x  ## override
##    x=5
##    print(x)
##
##local1()
##print(x)

##x=4
##def local1():
##    global x  ## override
##    x=5
##    print(x)
##
##local1()
##x=7
##print(x)


## decorator calling
def div(a,b):
    return float(a/b)

def smartdiv(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner
div1=smartdiv(div)

print(div1(5,9))


def my_deco(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper

def say():
    print("hello")

new1=my_deco(say)
new1()## function object


## closure
def multiplier_of(n):
    def multiply(num):
        return num*n
    return multiply

new=multiplier_of(6)
print(new(7))


