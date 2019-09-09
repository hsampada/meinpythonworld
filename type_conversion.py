#number reversing
##num=15783
##num=str(num)
##num[::-1]
##
##num=15783
##str(num)[::-1]  ### without changing type
##
##a=int(input("Enter number:"))
##b=int(input("Enter number:"))
##print(a+b)


## set without set
l1=[1,5,3,8,2,3,5,8,1,2]

l2=[0,0,0,0,0,0,0]
for i in range(len(l1)):
        if l1[i] in l2:
                continue
        else:
                l2[i]=l1[i]
                print(l2[i],end=" ")

#print(l1,l2)
