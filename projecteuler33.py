def curious(a,b):
    #We cancel trivial cases:
    if a >= b: return 0
    for i in range(len(str(a))):
        for j in range(len(str(b))):
            if str(a)[i] == str(b)[j] and i != j:
                if a*int(str(b)[:j]+str(b)[j+1:]) == b*int(str(a)[:i]+str(a)[i+1:]): return 1
    return 0
proda, prodb = 1, 1
for a in range(10,100):
    for b in range(10,100):
        if curious(a, b) == 1:
            print(str(a)+' ,'+str(b))
            proda *= a
            prodb *= b

i = 2
while i <= proda and i <= prodb:
    if proda%i == prodb%i == 0:
        proda//=i
        prodb//=i
        i = 1
    i += 1
print(str(proda)+', '+str(prodb))
