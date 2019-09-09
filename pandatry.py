import pandas as pd

ps=pd.Series([1,2,3,4,5])

ps1=pd.Series([5,6,7,8,9])

print(ps)
print(ps1)

df=pd.DataFrame({'name':['aahana','aaryana','advay','sampada'],'age':[2,1.5,7.5,32],'likes':['elephant','sheta','cars','movies']})
print ('\n',df)
df.insert(3,'food',['chocolate','fruit','poli','bhel'])
print('\n',df)

