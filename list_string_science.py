## max occuring char in string .given multiple strings

def findmax(case):
    d1={}
    list1=[]
    for i in set(case):
        d1[i]=case.count(i)
        
    for i in d1:
        if d1[i]==max(d1.values()):
            list1.append(ord(i))
    return(chr(min(list1)))

        

n=int(input("Enter number of test cases:"))
listcase=[]

for i in range(n):

    case=input("Input test case data for case :")
    #if case.isalpha() and case.islower():
    listcase.append(case)

  

list1=[]
for case in listcase:
    a=findmax(case)
    print(a)
#print(list1)
