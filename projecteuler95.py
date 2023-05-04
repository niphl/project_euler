def divSum(num):
    #we start by doing newton raphson to find the approximate square root of a
    x = num / 2
    lastroot = 0
    iterations = 0
    sum = 1
    while abs(x - lastroot) > 1:
        lastroot = x
        x = x / 2 + num / (2 * x)
        iterations += 19
    if (int(x//1))**2 == num: sum -= int(x//1)
    if (int(x//1)+1)**2  == num: sum -= int(x//1)+1
    for i in range(2, int(x//1)+1):
        if num%i == 0: sum += i + num//i
    return sum

maxCycleLength = 0
millionList = [1,]+[0,]*10**6 #1 shows we've been on the path
checkPointSize = 10**4
k = 1
for i in range(10**6+1):
    #the list checks whether we've been on this path before.
    if i > k*checkPointSize:
        k+=1
        print('Checkpoint '+str(k)+' passed')
    if millionList[i] == 0:
        pathHistory = tuple()
        j = i
        while divSum(j) < 1000001 and millionList[divSum(j)] == 0:
            pathHistory += j,
            millionList[j] = 1
            j = divSum(j)
        if divSum(j) in pathHistory:
            cycleLength = len(pathHistory)-pathHistory.index(divSum(j))+2
            if cycleLength > maxCycleLength:
                print(pathHistory[pathHistory.index(divSum(j)):])
                print('New max cycle Length of: '+str(cycleLength))
                x = min(e for e in pathHistory[pathHistory.index(divSum(j)):])
                print(x)
                maxCycleLength = cycleLength
