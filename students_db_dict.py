students={}
from tabulate import tabulate
while True:
    print("-"*150)
    choice=int(input("1. Add student data\n2. Display student data\n3. Remove student data\n4. Exit\nSelect option:"))
    print("-"*150)
    
    if choice==1:
    # adding new student
        roll=int(input("Enter roll number: "))
        if roll in students:
            print("Student data alredy present")
        else:
            students[roll]={}
            students[roll]={"name":input("Enter name of student: "),"marks":[int(input("Enter marks: "))],"degree":input("Enter degree:")}
            print("New student added",roll)
            
          

    elif choice==2:
    # displaying student
        roll=int(input("Enter roll number to display data: "))
        if roll in students:
            print(tabulate([students[roll].values()],headers=(students[roll].keys())))
        else:
            print("Student data not exist")
        
    elif choice==3:
    # remove data

        roll=int(input("Enter roll number to delete data: "))
        if roll in students:
            del(students[roll])
            
            print("Data deleted for roll no",roll)
        else:
            print("Student data not exist to delete")
    # exit
    elif choice==4:
        break
    else:
        print("Invalid input.Please give valid input.")
