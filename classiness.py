class classy():
    def __init__(self,item):
        self.item=[]
        self.item.append(item)
        print(self.item)
 
a=input("Have fancy item?y/n ")
while a=='y':
    item=input("Enter fancy item: ")
    classy(item)
