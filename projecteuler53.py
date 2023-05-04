def ncrgeqm(n,r):
    value = 1
    count = 0
    while count < r:
        value *= (n-count)/(r-count)
        if value > 10**6:
            return 1
        count += 1
    return 0
v = 0
for i in range(23,101):
    for j in range(1,i):
        v += ncrgeqm(i,j)
print(v)