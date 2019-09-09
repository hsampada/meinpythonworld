#strings
#name='SAMPADA'
##print(name[0:])
##print(name[1:3])
##print(name[0:5:2])#0 to 4 skipping 1 alternate
##print(name[:5])
##print(name[4::-1])
##print(name[-1::-1])#reverse string
##print(name[::-1])#same as above line
##print(name[:-3])

# List
##list1=['Aahana',1,4.5,67,'sampada',99.99]
##print(list1)
##print(list1[0])
##print(list1[:-1])#except last element
##print(list1[::-1])#reverse
##print(list1[::-2])
##print(list1[::2])
##list1[2]=5.5  ### mutable
##print(list1[2])
##print("list length: ",len(list1))


##tuple
##t1=(1,678,'sammy',90.90,'aaa',132334)
##print(t1)
##print(t1[1])
##print(t1[-1:-4:-1])
##print(t1[:-2])
##print(t1[1:4])
##print('tuple length: ',len(t1))
##print(t1[::-1])

###set
##s1={34,8989.978,34,78,34,78,45,'sammy','sammy'}
##print(s1)
##
###dictionary
##d1={"name":"sampada","num":12345,"marks":[57,67,87,97]}
##print(d1)
##print(d1["marks"][0])

##t1=(77,89,90)
##m1={"Maths":78,"English":t1}
##d1={"name":"sampada","marks":m1}
##print(d1)
##print("marks for english test 1:",d1["marks"]["English"][0])
##print(d1["marks"]["Maths"])
##print(d1.keys())
##


name=["sampada","Pooja","reema","Rahul","atul","Yogesh"]

rollno=list(range(1,7))
#print(rollno)
marks={"Maths":[78,89,67,90,75,89],"English":[90,78,80,74,85,80]}
students={"rollno":rollno,"name":name,"marks":marks}
#print(students)
print(students["rollno"][2])
print(students["name"][2])
print(students["marks"]["Maths"][2])
print(students["marks"]["English"][2])



























