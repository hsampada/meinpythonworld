str1=input()
n=int(str1)
d1={}
i=0
for i in range(len(str1)):
    d1[str1[i]]=int(str1[i])**3
print(d1)
if sum(d1.values())==n:
    print("Armstrong")
else:
    print("Not armstrong")
    
