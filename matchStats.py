import csv
import collections
from collections import Counter
from collections import defaultdict

class iplteam:
    
    def showTeam(self):
        infile=open("matches.csv")
        global teams,ind
        teams={}
        ind=1
        for line in infile:
            if line.split(',')[4] not in teams.values():
                teams[ind]=line.split(',')[4]
                ind+=1
                
        for i in teams:
            print(i,teams[i])
        sect=int(input("Select team: "))
        return(sect)

    def cal_Win(self):
        infile =open("matches.csv")
        
        
        l1=[]
        l2=[]
        l3=[]
        global mats #team,total number of toss win
        global tplay,twins #total maches
        global teamstat
        mats={}
        tplay={}
        twins={}
        teamstat=defaultdict(list)
        
        for line in infile:
           
            l1.append(line.split(',')[6])#total toss won
                   
            l2.append(line.split(',')[4])#total matches played
            l2.append(line.split(',')[5])#total matches played
            str1=line.split(',')[-1] 
            l3.append(str1.split('\n')[0])#total winner
        #print(mstat)    
                  
        mats=Counter(l1)
        tplay=Counter(l2)
        twins=Counter(l3)
        
        
        for d in (mats,tplay,twins):
            for key, value in d.iteritems():
                teamstat[key].append(value)
        #print(teamstat)
              
    def toss_Win(self,team):
        
        t=teams[team]
        return(t,teamstat[t][0],teamstat[t][1])
             

##m1=iplteam()
##t=m1.showTeam()
##m1.cal_Win()
##m1.toss_Win(t)
#print(Counter(l1))

    
##    def showTeam():
##        infile=open("matches.csv")
##        teams=[]
##        for line in infile:
##           t=line.split(',')[4]
##           teams.append(t)
##        for i in set(teams):
##            print(i)
##        sect=int(input("Select team: "))
##        return(sect)
