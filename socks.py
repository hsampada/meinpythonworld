import collections
n=int(input())
list1=[]
if n>=1 and n<=100:
    list1=list(map(int,input().split()))
    #if i>=0 and i<=100:
    
    d1=collections.Counter(list1)
    socks=0
    for i in d1.values():
        socks+=int(i/2)

    print(socks)
##    else:
##        print("wrong input")
else:
    print("wrong input")
