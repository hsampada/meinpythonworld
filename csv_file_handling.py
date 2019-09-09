## CSV file handling
import csv
##
##with open("chkcsv.csv","w") as my:
##    wr=csv.writer(my)
##    wr.writerow(["roll",1102,"name","Reema"])
##
##l1=["roll", '1102', '"name"', '"Reema"\n"roll"', '1103', '"name"', '"rani"\n"roll"', '1104', '"name"', "qqq"]
####writing single letter in coloumn for below
##with open(r"C:\Users\Sai\Documents\class_assignment\mycsv.csv","w") as my:
##	wr=csv.writer(my)
##	for i in l1:
##            wr.writerow(i)

##with open(r"C:\Users\Sai\Documents\class_assignment\mycsv.csv","r") as my:
##        rd=csv.reader(my)
##        print([i for i in rd])
##
##with open(r"C:\Users\Sai\Documents\class_assignment\mycsv.csv","a") as my:
##    wr=csv.writer(my)
##    wr.writerow(["roll", '1104', "name", "priyanka"])



## dict obj csv

d1={'roll':[1112,3121,2342],'name':['pooja','nisha','Nita']}

##for line in d1:
##    for i in d1[line]:
##        print(i)
with open("chkcsv.csv","a") as my:
        wr=csv.DictWriter(my,fieldnames=d1.keys())
        wr.writeheader()
        wr.writerow(d1)


            
#adding data to file from dict
##d1={'no':5,'name':'meena','add':'pune','sal':25000}
##myfile=open("employ.txt","a")
##wr=csv.DictWriter(myfile,fieldnames=d1.keys())
##wr.writerow(d1)
##myfile.close()
