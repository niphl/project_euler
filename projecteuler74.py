import math

a = [0]*(8*10**6)

def factSum(b):
    SUM = 0
    b = str(b)
    for i in range(len(b)):
        SUM += math.factorial(int(b[i]))
    return SUM

count = 0
for i in range(1, 10**6+1):
    j = i
    t = tuple()
    while j not in t:
        t += j,
        j = factSum(j)
    if len(t) == 60:
        count += 1
        print(t)
        """"
    for i in range(len(t)):
        if j == t[i] and j < 10**6+1:
            if i == 59:
                count+=1
                print(i)"""


print(count)