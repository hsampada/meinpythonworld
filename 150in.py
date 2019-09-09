import sys
print(sys.copyright )#prints copyright
print(sys.version_info)
import time
print(time.ctime())
import math
r=1.1
area=math.pi*r**2
print(area)

myfile=open(r"C:\Users\Sai\Documents\class_assignment\song.txt")
for i in myfile:
    print(i)

n=int(input("number: "))
sum=0
for i in range(1,4):
    sum+=int(str(n)*i)
print(sum)

str1=input("enter built in funct:")
print(help(str1))

import calendar
print(calendar.calendar (2019))
for i in calendar.day_abbr:
    print(i)
print(calendar.month(2017,7))
print(calendar.isleap(2019))
for i in calendar.day_name:
    print(i)

print([i for i in calendar.month_abbr])

import datetime
print(datetime.date(2019,9,1))
fdate=datetime.date(2019,9,1)
ldate=datetime.date(2019,8,1)
print(fdate-ldate)

r=5
v=4/3*math.pi*r**3 # volume of sphere
print(v)

n=float(input("number for abs val: "))
print(abs(17-n))


import matplotlib.pyplot as plt
#plt.Circle(3040,5)
import numpy as np
weightList=[35,47,90,56,78,61,49,69,53]
plt.hist(weightList,density=0.5, bins=20)

#plot.axis([20, 100, 0, 0.06])
#axis([xmin,xmax,ymin,ymax])
plt.xlabel('Weight')
plt.ylabel('Probability')
plt.show()



l3=['a','v','e','t']
print("".join(l3))

numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958,743, 527
    ]
for i in numbers:
    if i%2==0:
        print(i)
    elif i==237:
        break

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(set(i for i in color_list_1 if i not in color_list_2))

def trarea(b,h):
	return(b*h/2)

a=trarea(4,5)
print(a)

def fact(n): #gretest common divisor
	l5=[]
	for i in range(2,n+1):
		if n%i==0:
			l5.append(i)
	return(l5)

print(max(set(fact(54)).intersection(set(fact(27)))))


def lcm(a, b):
    i = a
    while i % b != 0:
        i += a
    else:
        return (i)


n1 = int(input("num for lcm: "))
n2 = int(input("num for lcm: "))
if n1 < n2:
    l = lcm(n1, n2)
else:
    l = lcm(n2, n1)
print("lcm:",l)

x=int(input("num for x: "))
y=int(input("num for y: "))
print((x+y)*2)

import getpass,os,sys
print(getpass.getuser())


for i,j,k in os.walk(r'C:\Users\Sai\Documents\class_assignment'):
	if 'access_modified_time.py' in k:
		print("file exist")
		break

print(sys.version)
print("cpus:",os.cpu_count())