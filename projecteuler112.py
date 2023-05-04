def bouncy(num):
    increasing, decreasing = 1,1
    for i in range(len(str(num))-1):
        if int(str(num)[i]) > int(str(num)[i+1]):
            increasing = 0
        elif int(str(num)[i]) < int(str(num)[i+1]):
            decreasing = 0
        if increasing == decreasing == 0:
            return 1
    return 0

bouncyCount, i = 0,1
while True:
    bouncyCount += bouncy(i)
    #if i == 1000: print('i: '+str(i)+', bouncy%: '+str(round(bouncyCount/i, 3)))
    if i%10**5 == 0: print('i: '+str(i)+', bouncy%: '+str(round(bouncyCount/i, 3)))
    if bouncyCount*100 == 99*i:
        print('99% reached, i: '+str(i))
    i += 1