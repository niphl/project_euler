def internalRec(w,l):
    total = 0
    for i in range(1, l+1):
        for j in range(1, w+1):
            total += i*j
    return total-2*10**6
a,b = 1,1000
print(internalRec(2,3)+2*10**6)
print(internalRec(a,b))
record = 2*10**6
while b >= a:
    if abs(internalRec(a,b)) < record:
        record = abs(internalRec(a,b))
        print('New record, a: '+str(a)+', b: '+str(b)+', record:'+str(record))
    if internalRec(a,b) > 0: b -= 1
    else: a += 1
