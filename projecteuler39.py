t = tuple()
for i in range(500):
    for j in range(i//2, i):
        for k in range(0, j):
            if i*i == j*j + k*k: t += (i+j+k),
maxi = 0
for i in range(1001):
    if maxi < t.count(i):
        maxi = t.count(i)
        print('Max perimeter: '+str(i))