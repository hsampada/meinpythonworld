

matchcount=0
def counter(N):
    global matchcount
    
    if N<=1:
        return #matchcount
    else:
        if N%2==0:
            matchcount+=N/2
            if N/2>1:
                counter(N/2)
        else:
            matchcount+=(N-1)/2
            if (((N-1)/2)+1)>1 :
                counter(((N-1)/2)+1)

        
        
            
T=int(input())
if T>=1 and T<=10:
    i=0
    while i in range(T):
        N=int(input())
        if N>=0 and N<=1000:
            i+=1
            counter(N)            
            print(matchcount) 
        else:
            print("not proper input")
        
else:
    print("Invalid test cases")
    











       




    
