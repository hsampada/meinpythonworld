from class_start import employee
class programmer(employee):
    def __init__(self,name,salary,prj):
        employee.__init__(self,name,salary)
        self.prj=prj

    def disp(self):  ## method overriding
        employee.disp(self)
        print("project:",self.prj)

class manager(employee): ## inheritence
    pass

p1=programmer("anaya",12000,'abcd')
p1.disp()
m1=manager("aamaya",3242)
m1.disp()
