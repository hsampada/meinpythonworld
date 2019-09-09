def lcm(a,b):
    n=a
    while a<a*b:
        if a%b==0:
            return(a)
        else:
            a+=n


def smartlcm(func):
     def smart(a,b):
        if a<b:
             a,b=b,a
        return (func(a,b))
     return smart

new1=lcm(2,9)
print(new1)
