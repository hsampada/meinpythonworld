###factorial
##def fact(n):
##    if n==1:
##        return (1)
##    else:
##        return(n*fact(n-1))
##        
##
##n=int(input("Enter no to find factorial:"))
##f=fact(n)
##print(f)
##
##
####file name ,print extension
##str1=input("Enter filename: ")
##list1=[]
##list1=str1.split('.')
##print(list1[1])
##
##
####  area of circle
##rad=int(input("Enter redius of circle:"))
##print(float(rad*3.14))


## unique no in , separated
##str1=input("Enter comma separated num:")
##print ([int(i) for i in str1.split(',') if str1.split(',').count(i)==1])

## frequency of word string then list  fill in dict
##str1=input("Enter stateent:")
##d1={}
##for word in set(str1.split()):
##    d1[word]=d1[str1.split().count(word)]
##print(d1)


def lcm(a,b):
    i=a
    while i%b!=0:
            i+=a
    else:
            return(i)
		
			
n1=int(input())
n2=int(input())
if n1<n2:
    l=lcm(n1,n2)
else:
    l=lcm(n2,n1)
print(l)
