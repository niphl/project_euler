#Unproven that we have the correct answer

n = 1

pents = []
targets = {}
DisDefined = False
while True:
    k = n * (3 * n - 1) // 2  # k is the new entry
    n += 1  # iterate n

    for i in targets.copy():  # We pop no longer possible targets
        if DisDefined and targets[i] > D:
            targets.pop(i)
        elif k == i:
            if DisDefined:
                D = targets[i]
            else:
                DisDefined = True
                D = targets[i]
            targets.pop(i)
            print(D)
            print(targets)
        elif k > i:
            targets.pop(i)
    for i in pents:
        if not DisDefined:
            if k-i in pents:  # We add to targets if k-i is pentagonal, and wait to see if k+i is possible.
                targets[k + i] = k - i
        elif k - i < D:
            if k - i in pents:
                targets[k + i] = k - i

    if DisDefined and k - pents[-1] > D:  # if k-pents[-1] > all remaining targets we can break
        stop = 1
        for i in targets:
            stop *= k - pents[-1] > targets[i]
        if stop == 1:
            print('END')
            break
    pents += (k,)