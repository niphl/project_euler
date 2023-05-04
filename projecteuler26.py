def recursionlength(i):
    while i%2 == 0: i //= 2
    while i%5 == 0: i //= 5
    count = 1
    dividing = 9
    while dividing%i != 0:
        dividing += 9*(10**count)
        count +=1
    return count

peak = 0
maxi = 0
for j in range(1,1000):
    if recursionlength(j) > peak:
        maxi, peak = j, recursionlength(j)
        print('New maximum: Number '+str(maxi)+', recursionlength: '+str(peak))