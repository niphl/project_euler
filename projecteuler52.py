ds = '0123456789'
counter, xpass = 0,0
while xpass == 0:
    x = '1'+str(counter)
    for i in range(2,7):
        ypass = 0
        y = str(i*int(x))
        for digit in ds:
            if(y.count(digit)!=x.count(digit)):
                break
        else: ypass = 1
        if ypass == 0:
            break
    else: xpass = 1
    counter += 1
print(x)