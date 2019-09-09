count=0

try:
    for count in range(1,10):
        assert count!=7,'no cant be 7'
        print(count)

except AssertionError as E:
    count+=1
    print(E)
else:
    pass
finally:
    while count<11:
        print(count)
        count+=1
    print("successfully completed")