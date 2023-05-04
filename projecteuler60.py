# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
with open('primeslist.txt', 'r') as f:
    primeList = tuple(map(int, f.readline()[1:-1].split(', ')))
def newtonRaphsonForBigNum(num): #Newton Raphson integer square root for big number
    x = num // 3000
    lastroot = 0
    iterations = 0
    while abs(x - lastroot) > 1:
        lastroot = x
        x = x//2 + num//(2*x)
        iterations += 1
    return x
def binary_position(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid+1
        elif arr[mid] > x:
            return binary_position(arr, low, mid - 1, x)
        else:
            return binary_position(arr, mid + 1, high, x)
    else:
        return low
def isPrime(num, low, high):
    global primeList
    mid = (high + low)//2
    #num, 0, 664579 for primes less than 10 million, 0, 78498 for first 1 million primes, 0, 9592 for first 100,000 primes, 0,1229 for first 10,000 primes
    if num < primeList[len(primeList)-1]: #Binary search if it's in our list
        if high >= low:
            if primeList[mid] == num: return 1
            elif primeList[mid] > num: return isPrime(num, low, mid-1)
            else: return isPrime(num, mid+1, high)
        else: return 0
    #Otherwise we do trial division up to the square root. We find apprxoimate square root via Newton-Raphson Method
    else:
        for i in range(primeList[binary_position(primeList, 0, 664579, newtonRaphsonForBigNum(num))]+1):
            if num%primeList[i] == 0:
                return 0
        return 1

def primePairCheck(a, b):
    if isPrime(int(str(a)+str(b)),0,664579) == 1 and isPrime(int(str(b)+str(a)),0,664579) == 1:
        return 1
    else: return 0


def pairedPrimesShort(a):
    global pairedPrimesList, primeList10000
    for i in primeList10000:
        if i > a and primePairCheck(a, i) == 1: pairedPrimesList += (a, i),
        print(str((a, i))+' added to pairedPrimesList')
"""
pairedPrimesList = tuple()
print(primeList)
primeList1000=primeList[:168]
primeList10000=primeList[168:1229]
print(primeList1000)
quadPrimesList = ((3, 7, 109, 673), (23, 311, 677, 827))
quintPrimesList = tuple()
for a in quadPrimesList:
    for b in primeList10000:
        if primePairCheck(a[0], b) == 1 and primePairCheck(a[1], b) == 1 and primePairCheck(a[2], b) == 1 and primePairCheck(a[3], b): quintPrimesList += (a[0], a[1], a[2], a[3], b),
print(quintPrimesList)
"""
primeList10000=primeList[1:1220]
primeList2000=primeList[1:263]
pairedPrimesList, triplePrimesList, quadPrimesList, quintPrimesList = tuple(), tuple(), tuple(), tuple()
for a in primeList2000: pairedPrimesShort(a)
#pairedPrimeList Reduction
"""
numCounts = tuple()
for a in pairedPrimeList: numCounts += (a[0], a[1])"""
for a in pairedPrimesList:
    for b in primeList10000:
        if b > a[1] and primePairCheck(a[0], b) == 1 and primePairCheck(a[1], b) == 1:
            triplePrimesList += (a[0], a[1], b),
            print(str((a[0], a[1], b)) + ' added to triplePrimesList')
for a in triplePrimesList:
    for b in primeList10000:
        if b > a[2] and primePairCheck(a[0], b) == 1 and primePairCheck(a[1], b) == 1 and primePairCheck(a[2], b) == 1:
            quadPrimesList += (a[0], a[1], a[2], b),
            print(str((a[0], a[1], a[2], b)) + ' added to quadPrimesList')
for a in quadPrimesList:
    for b in primeList10000:
        if b > a[3] and primePairCheck(a[0], b) == 1 and primePairCheck(a[1], b) == 1 and primePairCheck(a[2], b) == 1 and primePairCheck(a[3], b) == 1:
            quintPrimesList += (a[0], a[1], a[2], a[3], b),
            print(str((a[0], a[1], a[2], a[3], b)) + ' added to quintPrimesList')
print(quintPrimesList)
minSum = 99999
for i in quintPrimesList:
    minSum = min(minSum, sum(i))
print('Minimum Sum: '+str(minSum))
"""
# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/"""
