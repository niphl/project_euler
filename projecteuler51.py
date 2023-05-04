with open('primeslist.txt', 'r') as f:
    primeList = tuple(map(int, f.readline()[1:-1].split(', ')))

t = tuple()
for i in primeList[9592:78498]: #Primes from 100,000 to 1,000,000
    maxdigitrepeat = 0
    for j in range(10): maxdigitrepeat = max(maxdigitrepeat, str(i)[:-1].count(str(j)))
    if maxdigitrepeat >= 3:
        t += i,

t0, t1, t2, t3, t4, t5, t6, t7, t8, t9 = tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple()
print(t)
tnew = tuple()
for i in t: tnew += str(i),
print(tnew)
for i in tnew:
    if i[0] == i[1] == i[2]: t0 += i[3] + i[4] + i[5],
    if i[1] == i[2] == i[3]: t1 += i[0]+i[4]+i[5],
    if i[4] == i[2] == i[3]: t2 += i[0]+i[1]+i[5],
    if i[0] == i[2] == i[3]: t3 += i[1]+i[4]+i[5],
    if i[0] == i[3] == i[4]: t4 += i[1]+i[2]+i[5],
    if i[0] == i[2] == i[4]: t5 += i[1]+i[3]+i[5],
    if i[0] == i[1] == i[3]: t6 += i[2] + i[4] + i[5],
    if i[0] == i[1] == i[4]: t7 += i[2] + i[3] + i[5],
    if i[1] == i[3] == i[4]: t8 += i[0] + i[2] + i[5],
    if i[1] == i[2] == i[4]: t9 += i[0] + i[3] + i[5],

bigt = [t0, t1, t2, t3, t4, t5, t6, t7, t8, t9]
print(bigt)
def repeatCount(tup):
    peakCount = 0
    storedvalue = '0'
    for i in tup:
        if tup.count(i) >= 8: print(i)
    print(tup)

for i in bigt: repeatCount(i)
