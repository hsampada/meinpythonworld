a=88
b=99
print("A: ",a)
print(id(a))
print("B: ",b)

print(id(b))
c=a
a=b
b=c
print("\nswapped values\nA: ",a)
print(id(a))
print("B: ",b)
print(id(b))

a=a+b
b=a-b
a=a-b
print("\nswapped values\nA: ",a)
print("B: ",b)

a,b=b,a # assign
print("\nswapped values\nA: ",a)
print("B: ",b)
