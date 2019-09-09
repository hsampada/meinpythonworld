i=0
while i<5:
    try:
        num=input("enter num:")
        if num==3:
            raise ValueError,'do not enter 3'
    except ValueError as v:
        print v
        i+=1
