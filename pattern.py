##n=int(input("Enter level: "))
##n*=2
##for i in range(1,n,2):
##    print(' '*int((n-i)/2)+'*'*i+' '*int((n-i)/2))
##    

##list1=['aba','bb','cttrc','htti','njijn','mkololm']
##for str1 in list1:
##    if len(str1)>2:
##        l=len(str1)
##        if str1[0]==str1[l-1]:
##            print(str1)
##        


##input_string = input("Enter string to print: ")
##
### Print a string literal saying "Hello, World." to stdout.
##print('Hello, World.')
##
### TODO: Write a line of code here that prints the contents of input_string to stdout.
##print(input_string)


def staircase(n):
    for i in range(1,n+1):
        print(" "*(n+1-i)+"#"*i)
    

if __name__ == '__main__':
    n = int(input())

    staircase(n)
