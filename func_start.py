##def mysum(a,b):
##    print(a+b)
##
##a=int(input("Enter number:"))
##b=int(input("Enter number:"))
##mysum(a,b)
##
##print(mysum(a,b))# types 'none' as nothing returning

##def mysum(a,b):
##    return a+b
##
##a=int(input("Enter number:"))
##b=int(input("Enter number:"))
###print(mysum(a,b)) ## not printing none as returning value
##c= mysum(a,b)
##print(c)
##
##
##def mysum(a,b,c=9):
##    return a*b+c
##
##a=int(input("Enter number:"))
##b=int(input("Enter number:"))
##c=int(input("Enter number:"))
##d=mysum(a,b,c)
##print(d)
##d=mysum(a,b) # takes default value
##print(d)
##

##def addlist(list1):
##    return(sum(list1))
##
##list1=[]
##for i in range(5):
##    a=int(input("Enter number:"))
##    list1.append(a)
##
##num=addlist(list1)
##
##print(num)


## passing multiple string
##def addnum(*a):
##    num=0
##    for i in a:
##        for j in i:
##            num+=j
##
##    return num
##            
##
##list1=[]
##for i in range(3):
##    a=int(input("Enter number:"))
##    list1.append(a)
##
##list2=[]
##for i in range(3):
##    a=int(input("Enter number:"))
##    list2.append(a)
##
##num=addnum(list1,list2)# creates list of tuple
##print(num)


# passing num and string

def addtwo(*a):
    num=0
    str1=''
    for i in a:
        if type(i)==str:
            str1=str1+i
        else:
            num+=i

    return num,str1

num,str1=addtwo(1,2,'sampada',4,5,'aahana',2)
print(num,str1)











