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

def truncatable(a):
    if isPrime(a, 0, 78498) == 0 or len(str(a))==1: return 0
    #Left truncation
    b = str(a)[1:]
    while len(b) != 0:
        if isPrime(int(b), 0, 78498) == 0: return 0
        b = b[1:]
    #Right truncation
    b = str(a)[:-1]
    while len(b) != 0:
        if isPrime(int(b), 0, 78498) == 0: return 0
        b = b[:-1]
    return 1
sum = 0
for i in range(999999):
    if truncatable(i):
        print(i)
        sum+=i

print('Sum: '+str(sum))