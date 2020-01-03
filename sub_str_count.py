import collections
str1=input()
n=int(input())
count=0

count=collections.Counter(str1)['a']*int(n/len(str1))
r=n-(int(n/len(str1))*len(str1))
count+=collections.Counter(str1[:r])['a']

print(count)
