coinsizes = (2, 5, 10, 20, 50, 100, 200)
c = (1,)*201

for coinsize in coinsizes:
    c = tuple(c)
    ccopy = c
    print(c)
    c = [0, ] * 201
    for i in range(201):
        j = 0
        while i >= j:
            c[i] += ccopy[i - j]
            j += coinsize
    print(c)