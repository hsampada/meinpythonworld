
##import turtle
##ttl = turtle.Turtle()
##ttl.forward(100)
##ttl.right(90)
##ttl.forward(100)
##ttl.right(90)
##ttl.forward(100)
##ttl.right(90)
##ttl.forward(100)
##ttl.right(90)
##
##ttl = turtle.Turtle()
##ttl.circle(60)
##
##ttl.back(150)
##ttl.right(60)
##ttl.forward(150)
##ttl.right(60)
##ttl.back(150)
##ttl.right(60)

##for i in range(0,2):
##    
##    for j in range(0,4):
##        ttl.right(120)
##        ttl.forward(100)
##        ttl.right(120)
##        ttl.forward(100)
##        ttl.left(120)
##        ttl.forward(100)
##        ttl.right(120)
##        ttl.forward(100)
##    ttl.seth(180)



#from turtle import *

##ttl.color('blue', 'yellow')
##ttl.hideturtle()
##
##ttl.begin_fill()
##while True:
##    ttl.forward(150)
##    ttl.left(220)
##    if abs(ttl.pos()) < 1:
##        break
##ttl.end_fill()
##ttl.reset()

def caldit(str1):
    
#calculate digit ,letter
    
    #print(type(s))

    digit=0
    uchar=0
    lchar=0
    sym=0
    for i in str1:
        if i.isdigit():
            digit+=1
        elif i.isalpha():
            if i.isupper():
               uchar+=1
            else:
                lchar+=1
        else:
            sym+=1


    return(digit)
##print("character uppercase" ,uchar, "\n lowercase:",lchar)
##print("Symbols" ,sym)

# input as string
##givens=input("Enter string:")
##num=[i for i in givens.split()]
##print(num)


## whole number even
##givens=input("Enter number:")
##checks="02468"
##
###func allevedigit()
##if givens in checks:
##        print("all numbers even")
##else:
##        print("not all numbers even")

## bank account
##netammount=0
##transaction="yes"
##trans=[]
##while transaction=='yes':
##    givens=input("Enter transaction string:")
##    value=givens.split(" ")
##    
##    if value[0]=="D":
##        netammount+=int(value[1])
##       
##    else:
##        netammount-=int(value[1])
##        
##    transaction=input("Want to add more trasaction yes/no:")
##     
##
##
##print("net balance = ",netammount)


##yield
##import pdb
##def nextSquare(): 
##    i = 1; 
##  
##    # An Infinite loop to generate squares  
##    while True: 
##        yield i*i                 
##        i += 1  # Next execution resumes  
##        pdb.set_trace()        # from this point      
##  
### Driver code to test above generator  
### function
##
##for num in nextSquare(): 
##    if num > 100: 
##         break    
##    print(num)


###2 D array
##import numpy
##givens=input("enter dimension:")
##dimen=[x for x in givens.split(",")]
##rowlen=int(dimen[0])
##collen=int(dimen[1])
##print(dimen)
##ansdi=[[0 for j in range(collen)] for i in range(rowlen)]
##
##for i in range(rowlen):
##    for j in range(collen):
##        print(i,",",j)
##        #print(dimen[0],",",dimen[1])
##        ansdi[i][j]=i*j
##
##print(ansdi)



### turtle draw

##import turtle
##ttl=turtle.Turtle()
##ttl.color("red")
##print(ttl.position())
##ttl.goto(-250,200)
##ttl.fillcolor("yellow")
##ttl.begin_fill()
##ttl.circle(50)
##ttl.end_fill()
##bg=turtle.Screen()
##bg.bgcolor("light blue")

## sort
##tosort=[]
##while input("want to enter number :")== "yes":
##    tosort.append(int(input("Enter list of numbers to sort : ")))
##    
##print(tosort)
##j=0
##for j in range (0,len(tosort)-1):
##    
##    for i in range(0,len(tosort)-1):
##        j=i+1
##        if tosort[i]<tosort[j]:
##            j=j+1
##        else:
##            ex=tosort[i]
##            tosort[i]=tosort[j]
##            tosort[j]=ex
##            j=j+1
##        
##print(tosort)

#square root
##num=int(input("Enter number to find square root: "))
##sqrt=num**0.5
##print("Square root of ",num,"is ",sqrt)
##cubert=num**0.35
##print("Cube root of ",num,"is ",cubert)



## twilio
##
##import twilio
##print(twilio.__version__)


## opening web site
##import webbrowser
##webbrowser.open_new_tab("https://www.youtube.com/watch?v=daFg_rAy7J8")



##checking proficiency
##import urllib.request
##
####def check_pro(check_to):
##chresp= urllib.request.urlopen("http://www.wdylike.appspot.com/?q= "+ "spot" )
##outresp=chresp.read()
##print(outresp)
##chresp.close()

##myfile = open( "C:\\Users\\Sai\\Documents\\sampada\\priv\\word_to_check.txt")
##mfile=myfile.read()
##print(mfile)
##myfile.close()
##
###check_pro(mfile)
##
##

















































































