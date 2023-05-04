import math
fnew, fprevious = 1, 1
n = 2

phi = (math.sqrt(5)+1)/2
ffront = phi*phi/(math.sqrt(5))
ffront = int(str(ffront)[0] +str(ffront)[2:11])

print(ffront)
phi = int(str(phi)[0] +str(phi)[2:12])
print(phi)

print((((math.sqrt(5)+1)/2)**2749)/math.sqrt(5))

while n<3000:
    ffront = phi*ffront
    ffront = int(str(ffront)[:25])
    fpreviousCopy = fprevious
    fprevious = fnew
    fnew = fnew + fpreviousCopy
    n+=1
    fst = str(fnew)
    l = len(fst)
    fst = str(fnew)[l - 9:]
    if '1' in fst and '2' in fst and '3' in fst and '4' in fst and '5' in fst and '6' in fst and '7' in fst and '8' in fst and '9' in fst:
        print(n, fst, 'rear')
    fst = str(ffront)[:9]
    if '1' in fst and '2' in fst and '3' in fst and '4' in fst and '5' in fst and '6' in fst and '7' in fst and '8' in fst and '9' in fst:
        print(n, fst, 'front')
    if l > 10:
        fnew = int(str(fnew)[l-9:])