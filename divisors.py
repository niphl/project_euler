#Our program only takes integer inputs. We may need to change it later

a, b = 0,0
divisors = -1,
dpass = 0
validab = 0
integers = '0123456789'

while validab == 0:
    tup = tuple(input('a b: ').split(' '))
    if len(tup) != 2: a, b = 'error','error'
    else: a, b = tup[0], tup[1]
    for i in a:
        if i not in integers:
            a = -1
            continue
    for i in b:
        if i not in integers:
            b = -1
            continue
    a, b = int(a), int(b)
    if 0 < a and a < b:
        validab = 1

while dpass == 0:
    divisors = tuple(map(int, input('Divisors: ').split(' ')))
    dpass = 1
    for d in divisors:
        if d < 1 or d > b: dpass = 0

divisors = sorted(divisors)

print('M', end ='')
for d in divisors: print(' '+str(d), end='')
print('')
for i in range(a, b):
    print(str(i),end='')
    for j in divisors:
        print(' '+str(int(i%j == 0)), end='')
    print('')