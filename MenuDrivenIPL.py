import matchStats


while True:
    print '===Statistics==='
    print '1. Toss Winning Stats'
    print '2. Yearwise matches played/won'
    print '3. Citywise Matches played/won'
    print '4. Exit'
    choice=input('Enter a choice: ')


    if choice==1:
        team=matchStats.iplteam()
        t=team.showTeam()
        team.cal_Win()
        listToss=team.toss_Win(t)
        print '*'*60
        print "%s won toss %s times in %s matches.\nHence toss winning percentage is %.2f" %(listToss[0],listToss[1],listToss[2],float(listToss[1])/listToss[2]*100)+"%"
        print '*'*60
        continue

            
##    if choice==1:
##        team=matchStats.iplteam.showTeam()
##        listToss = matchStats.toss_Win(team)
##        print '*'*60
##        print "%s won toss %s times in %s matches.\nHence toss winning percentage is %.2f" %(team,listToss[1],listToss[0],float(listToss[1])/listToss[0]*100)+"%"
##        print '*'*60
##        continue
##    elif choice==2:
##        team=matchStats.showTeam()
##        yearMatch = matchStats.yearwise_Wonplayed(team)
##        print '*'*60
##        print team
##        print ' '*3,"YEAR",' '*7,"MATCHES PLAYED",' '*7,"MATCHES WON"
##        
##        yearMatch.sort()
##        for value in yearMatch:
##            print "%s %s %s %02d %s %02d"%(' '*3,value[0],' '*12,value[1],' '*18,value[2])
##        print '*'*60
##        continue
##    elif choice==3:
##        team = matchStats.showTeam()
##        cityMatch = matchStats.locationwise_Wonplayed(team)
##        print '*'*60
##        print team
##        print ' '*10,"CITY",' '*7,"MATCHES PLAYED",' '*7,"MATCHES WON"
##        cityMatch.sort()
##        for value in cityMatch:
##            print "{:>16}  {:>12}{:02d}  {:>17}{:02d} ".format(value[0],'',value[1],'',value[2])
##        print '*'*60
##        continue
##    elif choice==4:
##        print 'Thanks for exploring our site. Do visit again...!!!!'
##        break
##    else:
##        print 'Invalid Choice'
