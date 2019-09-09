import requests,json
from statistics import mean
import matplotlib.pyplot as plt
import numpy as np
from functools import reduce

def dsort(n):
        at={}
        for i in jrs['dataset']['data']:
                for dt in i:
                        if type(dt)==str:
                                yr=dt.split('-')[0]
                                if yr in at:
                                        at[yr].append(i[n])
                                else:
                                        at[yr]=[i[n]]
        return(at)
        
def closedt():
        at=dsort(-3)
        

        for j in at:
                at[j]=mean(at[j])
        print(at)
##        l=[]	
##        for i in at:
##                l.append(at[i])
##        plt.hist(l,density=0.5,bins=20)
##
##        plt.show()

        

def trademax():# total trade quantity max  yearly
        at=dsort(-2) 
        for i in at:
                num=reduce(lambda x,y:max(x,y),at[i])
                for j in jrs['dataset']['data']:
                        if j[6]==num:
                                print(j)


res=requests.get('https://www.quandl.com/api/v3/datasets/NSE/INFY.json?api_key=fKXsYh9Qi9ySbS8X6pNh')
jrs=json.loads(res.text)
closedt()
trademax()
