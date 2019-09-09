##print("i can print here")
##saving = 100
##result = saving + saving * 0.1
##print("return on investment = " , result)

##name age         #####
##name=input("Enter ur name : ")
##print ("Hi " + name)
##age=int(input("Enter age :"))
##year=2019-age
##print (("your birth year is " ,year ) *2)


##even odd############
##number=int(input("enter number: "))
##remainder=number %2
##if remainder == 0:
##   print("the given number is even")
##
##else:
##   print ("the number is odd")



###list####

##list1=[]
##for i in range(0,5):
##   num=int(input("enter number for list :"))
##   list1.append(num)
##
##print(list1)
##print("length of list :" ,len(list1))
##print("Max no of list :" ,max(list1))
##print("min no of list :" ,min(list1))

### divisor / prime number

##def divisor(num):
##              num1=int((num/2)+1)
##              list2=[]
##              for i in range(1,num1):
##                    if num%i==0:
##                      
##                      list2.append(i)
##
##              if len(list2)>2:
##                  print("Given number is not prime")
##                  print("Divisor are:" ,list2)
##              else:
##                  print("The number", num,"is prime")
##              return;
##
##try:
##         num=int(input("enter number: "))
##         divisor(num);
##
##except:
##    if ValueError:
##        num=int(input("Please enter valid number: "))
##        divisor(num);
#############################################################          

##common list

##    list1=[]
##    list2=[]
##    list3=[]
##    for i in range (1,5):
##       list1.append(int(input("enter list 1 number: ")))
##
##    print("List 1 is ", list1)
##    for i in range (1,5):
##       list2.append(int(input("enter list 2 number: ")))
##
##    print("List 2 is ", list2)
##
##    for i in list1:
##        if i in list2:
##            list3.append(i)
##
##    print("Common elements are :", list3)

###palindrome
##
s1=input("Enter string: ")
print(s1)
if s1 == s1[::-1]:
    print("string is palindrome")
else:
    print("not palindrome")
              

##
####list comprehension

##list1=[1,2,4,5,6,8,9,10]

##list2=[no for no in list1 if no%2==0 ]
##print(list2)

## rock,paper,scissor

##user="yes"
##
##while (user=="yes"):
##        player1=str(input("Enter player 1 rock/paper/scissor: "))
##        player2=str(input("Enter player 2 rock/paper/scissor: "))
##        if player1==player2:
##            print("game tie")
##            user=str(input("want to play more yes/no : "))
##        elif player1=="rock" and player2=="scissor":
##             print("player 1 wins")
##             user=str(input("want to play more yes/no : "))
##             
##        elif player1=="scissor" and player2=="paper":
##             print("player 1  wins")
##             user=str(input("want to play more yes/no : "))
##             
##        elif player1=="paper" and player2=="rock":
##             print("player 1  wins")
##             user=str(input("want to play more yes/no : "))
##             
##        else:
##             print("player 2 wins")
##             user=str(input("want to play more yes/no : "))

###guessing number
##import random
##
##myno=str(random.randint(1111,9999))
####gno=str(input("guess the no:"))
##p=0
##c=0
##
###print(myno)
##while p<4:
##     gno=str(input("guess the no:"))
##     p=0
##     c=0
##     for i in range(0,4):
##        if gno[i]==myno[i]:
##            p=p+1
##
##        elif gno[i]in myno:
##            c=c+1
##     print("you guessed",p,"right position digit and digit",c)
##     
##     
##
##
##print(type(myno))
##print ("guessed the right number.Number is ",myno)
##
    
#sets to list
##number1 = [2,5,7,8,6,9,9,4,3,2,5,8,7,6,4,9,0]
##number2 = [3,5,6,8,11,10,47,7,5,6,80]
####print("original: ",number)
##number1=set(number1)
##number2=set(number2)
####print("set: ",number)
####print(len(number))
##
##print("common are",number1 in number2 )

## password generator
##import secrets
##import string
##i=0
##char=int(input("enter password length: "))
##print(char)
##print( secrets.choice(string.ascii_letters+string.digits) for i in range(char))


##from bs4 import BeautifulSoup
##import requests
##ttl_lst = []
###with open ('https://www.practicepython.org/' ) as html_file:
##soup = BeautifulSoup(requests.get('http://www.nytimes.com/').text)
##
##
##title = soup.findAll('h3')
##
##for row in title:
##
##     ttl_lst.append(row.text)
##
##print( ttl_lst)

##writing to file
##with open("write_to_file","W") as fwrite:
##     fwrite.write(input("enter string"))


##with open("write_to_file","r") as fwrite:
##     print(fwrite.read())
##
##with open("write_to_file","r+") as fwrite:
##     fwrite.write(input("enter string"))
##
##with open("write_to_file","r") as fwrite:
##     print(fwrite.read())


#divisible by 7 but not by5
##import os
##import psutil
##
##num=[]
##for i in range(2002,3201):
##    if i%7==0 and i%5!=0:
##        num.append(i)
##    
##print(num)
##
##num=[]
##
##for i in range(2002,3201,7):
##    if i%7==0 and i%5!=0:
##        num.append(i)
##    
##print(num)


##n*n-1
##def fact(x):
##
##    if x == 0:
##
##        return 1
##
##    return x * fact(x - 1)
##
##
##
##x=int(input("enter number: "))
##
##print (fact(x))

##numsquare={}
##num=int(input("enter number:"))
##for i in range (1,num+1):
##    numsquare[i]=i*i
##
##print(numsquare)

























