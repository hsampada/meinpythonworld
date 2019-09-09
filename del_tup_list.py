def deltup(l1):
    l2=l1.copy
    for i in range(6):
        
        if type(l1[i])== tuple and len(l1[i])==0:
            #print(l1[i])
            del(l1[i])
            
            

    print(l1)


l1=[1,2,4,7,(),9]
print(l1)
deltup(l1)
#print(l1)

            
