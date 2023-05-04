"""length = 501
coinsizes = range(2,length)
c = (1,)*(length+1)
for coinsize in coinsizes:
    c = tuple(c)
    ccopy = c
    c = [0, ] * (length+1)
    for i in range(length+1):
        j = 0
        while i >= j:
            c[i] += ccopy[i - j]
            j += coinsize
    print(c)"""

length = 501
coinsizes = range(2,length)
c = (1,)*(length+1)
for coinsize in coinsizes:
    c = tuple(c)
    ccopy = c
    c = [0, ] * (length+1)
    for i in range(length+1):
        j = 0
        while i >= j:
            c[i] += ccopy[i - j]
            j += coinsize
    print(c)