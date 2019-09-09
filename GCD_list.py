def fact(n): #gretest common divisor
	l5=[]
	for i in range(1,n+1):
		if n%i==0:
			l5.append(i)
	return(l5)

print(max(set(fact(5)).intersection(set(fact(7)))))