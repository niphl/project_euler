def rmax(a):
    x = 1
    y = 1
    peak = 0
    xyhistory = tuple()
    for i in range(a**2):
        x *= a-1
        x %= a**2
        y *= a+1
        y %= a**2
        if (x+y)%(a**2) > peak:
            peak = (x+y)%(a**2)
        elif (x,y) in xyhistory:
            break
        xyhistory += (x, y),
    return peak
rsum = 0
for i in range(3,1001):
    rsum += rmax(i)
    if i%50 == 0: print(i, rmax(i))
print(rsum)