
def generateSieve():
    i = 2
    n = 10**7
    global primeList
    A=[0,0]+[1,]*n
    while i*i <= n:
        if A[i] == 1:
            primeList += i,
            print('Added '+str(i)+' to list of primes.')
            j = i*i
            while j <= n:
                A[j] = 0
                j += i
        i += 1
    for k in range(i, n):
        if A[k] == 1:
            print('Added ' + str(k) + ' to list of primes.')
            primeList += k,
primeList = tuple()

generateSieve()
print(primeList)
with open('primeslist.txt', 'w') as f:
    f.write(str(primeList))

with open('primeslist.txt', 'r') as f:
    y = tuple(map(int, f.readline()[1:-1].split(', ')))

print(y)
