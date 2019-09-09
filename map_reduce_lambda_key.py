l1 =['1','10','11','5','7']
##sorted(l1)
##['1', '10', '11', '5', '7']
##l1 =['1','10','5','7','2','11',]
##
##sorted(l1)
##['1', '10', '11', '2', '5', '7']
##sorted(l1,key(int))
##
####Traceback (most recent call last):
####  File "<pyshell#4>", line 1, in <module>
####    sorted(l1,key(int))
####NameError: name 'key' is not defined
##sorted(l1,key=int)
##['1', '2', '5', '7', '10', '11']


##num=reduce(lambda x,y:x+y,range(1,11))
##print(num)
##
###factorial
##num=reduce(lambda x,y:x*y,range(2,6))
##print(num)
##
### Max num
##num=reduce(lambda x,y:x if x>y else y,l1)
##print(num)


state=['gujrat','Maha','raj']
capital=['gandhi','mum','jai']
print({x:y for x,y in zip(state,capital)})

print([chr(i)for i in range(65,65+26)])

print{i-64:chr(i)for i in range(65,65+26)}
