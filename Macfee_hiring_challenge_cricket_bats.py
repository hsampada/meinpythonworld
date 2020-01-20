'''
Mr Ski is a famous Cricket Bat manufacturer in Meerut. He has been in the business for a long time now.
He has been developing the special bats with the changing times to meet up the expectations of the players. He was researching for
a while to develop new kind of bats as the cricket is moving at a fast pace and he has to maintain his reputation and quality of bats.
He has developed special kind of bats and the word has spread all over the city.
The bats have a weight which provides the balance to the cricketer and are ready to use. The bats can be directly put to action without knocking.
There are N such bats with each bat having a weight Wi and a minimum price Mi. Mr Ski knows the worth of his bats and has decided to sell only
one bat per person.
'''


bats={}
req={}
l=list(input().split())
N=int(l[0])
C=int(l[1])
if N>=1 and N<=1000 and C>=1 and C<=1000:
    i=0
    while i in range(C):
        l=list(input().split())
        if int(l[0]) and int(l[1]) in list(range(1,10**6)): 
            req[int(l[0])]=int(l[1])
            i+=1
        else:
            print("wrong input")
        

    #print(req)
    i=0
    while i in range(N):
        l=list(input().split())
        if int(l[0]) and int(l[1]) in list(range(1,10**6)): 
            bats[int(l[0])]=int(l[1])
            i+=1
        else:
            print("wrong input")
    #print(bats)
    
    totalbats=0
    for i in req.keys():
        for j in bats.keys():
            if i<j and req[i]>bats[j]:
                totalbats+=1
                break
    print(totalbats)
else:
    print("wrong input")
