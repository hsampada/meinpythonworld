
box={'A':[5,2,7],
     'B':[4,3,8],
     'C':[9,1,2]
    }
count =0

#print(sum(box['A']))
      
## total sum - index[j] value

for i in box:
##   for j in range(3): 
    if i=='A':
        count=sum(box[i])- box[i][0]
        print(sum(box[i]),box[i][0],count)
##        if box[i][1]>0 :
##            count=count+box[i][1]
##        if box[i][2]>0:
##            count=count+box[i][2]
    elif i=='B':
        count+=sum(box[i])- box[i][1]
        print(sum(box[i]),box[i][1],count)
##         if box[i][2]>0:
##            count=count+box[i][2]
##         if box[i][0]>0 :
##            count=count+box[i][0]
    else:
        count+=sum(box[i])- box[i][2]
        print(sum(box[i]),box[i][2],count)
##         if box[i][1]>0 :
##            count=count+box[i][1]
##         if box[i][0]>0 :
##            count=count+box[i][0]
print(count)

