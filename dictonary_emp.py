names=["sampada","jyoti","purva","aabha","smriti"]
num=[23,6,34,43,78]
dep=["aa","bb","cc","dd","ee"]
sal=[20922,89037,99743,4787,38980]
emp_d1={"names":names,"num":num,"dep":dep,"sal":sal}
print(emp_d1)
print("Employee names: ",emp_d1["names"])
print("Employee number: ",emp_d1["num"])
print("Empployee dept: ",emp_d1["dep"])
print("Employee salary: ",emp_d1["sal"])

print(emp_d1["names"][1],emp_d1["num"][1],emp_d1["dep"][1],emp_d1["sal"][1])


## key-value exchange
for i,j in d1.items():
	if j in d2:
		d2[j].append(i)
	else:
		d2[j]=[i]
