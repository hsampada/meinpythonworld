students={}
import csv
##class studentsdb:
##    def __init__(self,roll,name,subject,marks):
##        self.roll=roll
##        self.name=name
##        self.subject=subject
##        self.marks=marks
##
##    def dispstudent(self):
##        print(self.roll,self.name,self.subject,self.marks)
##        s1=studentsdb(int(input("roll number:")),input("Name: "),input("subject: "),input("marks: "))
##with open("stud.csv","a")as me:
##                    wr=csv.DictWriter(me,fieldnames=students.keys())
##                    wr.writeheader()
##                    wr.writerow(students)
try:
    while True:
        print(" "*50,"Menu")
        print("-"*100,"\n1.Add new student\n2.Search student\n3.Remove student data\n4.Exit\n","-"*100)
        ch=int(input())
        if ch==1:
            roll=int(input("roll number:"))
            if roll in students:
                print("data already present.\n",students[roll])
            else:
                     
                students[roll]={}
                students[roll]={"name":input("Name: "),"subject":input("subject: "),"marks":input("marks: ")}
                print("Info added")

        elif ch==2:
            n=int(input("Roll number: "))
            if n in students:
                print(students[n])
                        
        elif ch==3:
            n=int(input("roll number: "))
            if n in students:
                del(students[n])
                print("Info deleted for ",n)
            else:
                print("there is no info for roll number ",n)
                
        elif ch==4:
            break

        else:
            print("invalid choice")
            
except Exception as E:
    print(E)

    
