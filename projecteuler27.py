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
    #while num > primeList[len(primeList)-1]: updatePrimeList()
    #0, 664579 starting inputs for low high
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

def maxc(a, b):
    count = 0
    while isPrime(count*count+a*count+b,0, 664579) == 1: count += 1
    return count

peak = 0

for a in range(-999,1000):
    for b in range(-1000,1000):
        if maxc(a,b) > peak:
            peak = maxc(a,b)
            print('New maximum of '+str(peak)+' from pair '+str(a)+','+str(b))
print(progra)