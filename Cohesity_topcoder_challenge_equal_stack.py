'''
Given number of stacks to make equal length by removing upper values
'''

def calm(listn,n):
    if sum(listn)>n:
        calm(listn[1:],n)
    else:
        print(listn)





list1=[5,4,2,1]
list2=[1,2,5,2]
list3=[9,7]
n=sum(list1)-list1[0]

calm(list2,n)
calm(list3,n)


