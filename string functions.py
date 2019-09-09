## string functions

case=input()
count,count1,count2,count3=0,0,0,0
for i in case:
	if i.isupper():
		count+=1
	elif i.islower():
		count1+=1
	elif i.isnumeric():
		count2+=1
	else:
		count3+=1

print(count,count1,count2,count3)


## List functions

