#reverse digit of integer
def rev(str1):
#str1='321'
  return("".join(i for i in str1[::-1] if str1[-1]!='0'))

if __name__=='__main__':
    
    # removing vowel from string
    str1='I like to eat apple and banana'
    print(" ".join(x for x in str1 if x not in ('aeiouAEIOU')))

    #max number in list
    list1=[98,56,78,34,1323,345]
    #print(reduce(lambda x,y: x if x>y else y,list1))# works in 2.7
    from functools import reduce
    print(reduce(lambda x,y: x if x>y else y,list1))

    #word with length in dict
    str1='I like to eat apple and banana'
    print({i:len(i)for i in str1.split(' ')})


