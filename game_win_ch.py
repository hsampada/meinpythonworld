## game win challenge
import itertools

t1=int(input())
if t1>=1 and t1<=10:
    
    result=[]
    for t in range(t1):
        str1=input()
        r=int(str1.split()[0])
        if r>=1 and r<=1000:
            p=int(str1.split()[1])
            if p>=1 and p<=r:
                num=0
                flag=True
                l4=itertools.product(['A','B'],repeat=r)
                for i in l4:
                    if i.count('A')>(i.count('B'))*p:
                       for k in range(p):
                           if i[k]!='A':
                                flag=False
                                
                       else:
                           if flag==True:
                               num+=1
                result.append(num)
     for i in result:
            print(i)
             
