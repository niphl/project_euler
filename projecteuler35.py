with open('primeslist.txt', 'r') as f:
    primeList = tuple(map(int, f.readline()[1:-1].split(', ')))

print(primeList[78498]) #First prime number over 1 million is in index 78498

shortListPrimes, circlePrimes = set(), {'2', '5'}
for i in primeList[:78498]:
    if  str(i).find('2') == str(i).find('4') == str(i).find('6') == str(i).find('8') == str(i).find('5') == str(i).find('0') == -1:
        shortListPrimes.add(str(i))

print(shortListPrimes)
print(len(shortListPrimes))

for i in shortListPrimes:
    if len(i) == 1: circlePrimes.add(i)
    else:
        iPassed = 1
        cycledNum = i
        for j in range(len(i)-1):
            cycledNum = cycledNum[-1]+cycledNum[:-1]
            if cycledNum not in shortListPrimes:
                iPassed = 0
                print(cycledNum+' not found!')
        if iPassed == 1: circlePrimes.add(i)

print(circlePrimes)
print(len(circlePrimes))