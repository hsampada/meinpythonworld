## file handling

##file=open("C:\HaxLogs.txt")
##print(file.read()) ## gives full file
##file.seek(0)
##print(file.readline())  ## line by line
##file.seek(0)
##print(file.readlines())  ## list of stringsof each line in file
##file.seek(0)
##for i in file:  ## full file iterating over file
##    print(i)


##file.write(file.read())
##for i in file:  ## full file iterating over file
##    print(i)


## os
import os
#print(os.getcwd())
#for each in os.walk(os.getcwd()):
#print (each)

for a,b,file1 in os.walk(os.getcwd()):
    print(file1)
    for i in file1:
        if i.split('.')[-1]=='py':
            print(i)
    




