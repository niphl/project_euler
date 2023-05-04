p3, p4, p5, p6, p7, p8 = set(), set(), set(), set(), set(), set()
a = 0
t = [p3, p4, p5, p6, p7, p8]
t = t[::-1]
for a in range(len(t)):
    i = 0
    while i*((a+1)*i+1-a)//2 < 10000:
        if i*((a+1)*i+1-a)//2 > 999: t[a].add(str(i*((a+1)*i+1-a)//2))
        i+=1

grandSet, grandSet2 =set(), set()
def checkCycles(t):
    global grandSet
    for e8 in t[0]:
        tempset, tempset2 = set(), {e8}
        for i in range(1, len(t)):
            for e in tempset2:
                for e2 in t[i]:
                    if e2[2:] == e[:2]:
                        tempset.add(e2 + e)
            tempset2, tempset = tempset, set()
        for e in tempset2:
            if e[-2:] == e[:2]: grandSet.add(e)

def permute(store, l):
    numstemp=l
    for i in range(len(l)):
        l = [numstemp[i],]+numstemp[:i]+numstemp[i+1:]
        if len(l) > 2: permute(store + [l[0],], l[1:])
        else: checkCycles(store + l)

permute([], t)
print(grandSet)
SUM = 0
for i in grandSet:
    for j in range(6):
        grandSet2.add(i[(4*j):(4*j+4)])
for i in grandSet2:
    SUM += int(i)
print(SUM)