class stud:
	def __init__(self,gname,groll):
		self.name=gname
		self.roll=groll
	def dispinfo(self):
		print("name:",self.name)
		print("roll:",self.roll)


class employee:
    empcnt=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        employee.empcnt+=1
    def disp(self):
        print("emp name:",self.name)
        print("emp salary:",self.salary)
        

##if __init__== '__main__'

##s1=stud("sampada",11)
##s1.dispinfo()
##print(s1.__dict__)
##s1.dept='IT'
##print(s1.__dict__)
##
####e1=employee("sampada",50000)
####e2=employee("ahana",1000000)
####e1.disp()
####print(e2.empcnt)
##
##
##
##student={}
##for i in range(3):
##    student[i]=stud(input("enter name:"),int(input("roll name:")))
##
##for i in student:
##    student[i].dispinfo()
##
