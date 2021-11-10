from math import exp
import random
import statistics
# C1: average = 9, standard deviation = 3
# C2: average = 7, standard deviation = 5
# C3: average = 11, standard deviation = 7
C1mean = 9
C1std = 3
C2mean = 7
C2std = 5
C3mean = 11
C3std = 7

def exploitOnly():
    list = [random.normalvariate(C1mean, C1std), random.normalvariate(C2mean, C2std), random.normalvariate(C3mean, C3std)]
    if max(list) == list[0]:
        list.extend([random.normalvariate(C1mean,C1std) for i in range(297)])
    elif max(list) == list[1]:
        list.extend([random.normalvariate(C2mean,C2std) for i in range(297)])
    else:
        list.extend([random.normalvariate(C3mean,C3std) for i in range(297)])
    return sum(list,0)

#print(exploitOnly())
#print(len(exploitOnly()))

def exploreOnly():
    list = [random.normalvariate(C1mean,C1std) for i in range(100)]
    list.extend([random.normalvariate(C2mean,C2std) for i in range(100)])
    list.extend([random.normalvariate(C3mean,C3std) for i in range(100)])
    #return list
    return sum(list,0)

#print(exploreOnly())

def eGreedy(p1:int):
    list = [random.normalvariate(C1mean, C1std), random.normalvariate(C2mean, C2std), random.normalvariate(C3mean, C3std)]
    if max(list) == list[0]:
        for i in range(297):
            if random.normalvariate(0,300) > 3*p1:
                list.extend([random.normalvariate(C1mean,C1std)])
            else:
                list.extend([random.choice([random.normalvariate(C1mean,C1std),random.normalvariate(C2mean,C2std),random.normalvariate(C3mean,C3std)])])
    elif max(list) == list[1]:
        for i in range(297):
            if random.normalvariate(0,300) > 3*p1:
                list.extend([random.normalvariate(C2mean,C2std)])
            else:
                list.extend([random.choice([random.normalvariate(C1mean,C1std),random.normalvariate(C2mean,C2std),random.normalvariate(C3mean,C3std)])])
    else:
        for i in range(297):
            if random.normalvariate(0,300) > 3*p1:
                list.extend([random.normalvariate(C3mean,C3std)])
            else:
                list.extend([random.choice([random.normalvariate(C1mean,C1std),random.normalvariate(C2mean,C2std),random.normalvariate(C3mean,C3std)])])
    return sum(list)
    #return sum(list,0)

#print(eGreedy(12))

def Simulation(trials:int, x:int) -> str:
    exploitlist = [exploitOnly() for i in range(trials)]
    explorelist = [exploreOnly() for i in range(trials)]
    greedylist = [eGreedy(x) for i in range(trials)]
    #print(exploitlist)
    #print(explorelist)
    #print(greedylist)
    return("Exploit Best: {exploitbest} \nExploit Mean: {exploitmean} \nExploit Regret: {exploitregret} \nExplore Best: {explorebest} \nExplore Mean: {exploremean} \nExplore Regret: {exploreregret} \nGreedy Best: {greedybest} \nGreedy Mean: {greedymean} \nGreedy Regret: {greedyregret}"\
        .format(exploitbest = (42+(18*297)), exploitmean = statistics.mean(exploitlist), exploitregret = (3300-statistics.mean(exploitlist)), \
            explorebest = (42*100), exploremean = statistics.mean(explorelist),exploreregret = (3300-statistics.mean(explorelist)), \
                greedybest = (18*300), greedymean = statistics.mean(greedylist),greedyregret = (3300-statistics.mean(greedylist))))

print(Simulation(100,12))
print("-----------------------------------------------------" )
print(Simulation(10000,12))
print("-----------------------------------------------------" )
print(Simulation(100000,12))

def findbestegreedy():
    index = 0
    emax = 0
    for i in range(0,101):
        a = eGreedy(i)
        if a > emax:
            emax = a
            index = i
    return index
    # + " " + str(list.index(max(list))
def bestxpercent(x:int):
    list = []
    for i in range(x):
        list.append(findbestegreedy())
    a = statistics.mode(list)
    return a

def bestpercent(x:int):
    list = []
    for i in range(x):
        list.append(bestxpercent(x))
    return ("Mean: {meana}\nStandard Deviation: {stdev}".format(meana = statistics.mean(list), stdev = statistics.stdev(list)))

print("-----------------------------------------------------" )
#print(bestpercent(10))