tn = 285
pn = 165
hn = 143

t, p, h = 40755, 40755, 40755

def increaset():
    global t, tn
    t += tn + 1
    tn += 1

def increasep():
    global p, pn
    p += 3 * pn + 1
    pn += 1

def increaseh():
    global h, hn
    h += 4 * hn + 1
    hn += 1

increaset()

while True:
    if t == p == h:
        print(t)
        print('END')
        break
    if t < p:
        increaset()
        print('t',t)
    elif p < h:
        increasep()
        print('p',p)
    elif h < t:
        increaseh()
        print('h',h)