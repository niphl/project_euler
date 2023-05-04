a,b,c,d = 1,2,3,4
l = '1234'
ops = ('+', '-', '*', '/')
def maxConsec(l):
    outputs = set()
    for i1 in tuple(l):
        l1 = list(l)
        l1.remove(i1)
        for o1 in ops:
            for i2 in l1:
                l2 = l1.copy()
                l2.remove(i2)
                for o2 in ops:
                    for i3 in l2:
                        l3 = l2.copy()
                        l3.remove(i3)
                        for o3 in ops:
                            for i4 in l3:
                                outputs.add(eval(i1+o1+i2+o2+i3+o3+i4))
                                comb1 = eval(i1+o1+i2)
                                comb2 = eval('comb1'+o2+i3)
                                try:
                                    comb3 = eval('comb2'+o3+i4)
                                    outputs.add(comb3)
                                except ZeroDivisionError: pass
                                try:
                                    comb3 = eval(i4+o3+'comb2')
                                    outputs.add(comb3)
                                except ZeroDivisionError: pass
                                comb2 = eval(i3+o2+'comb1')
                                try:
                                    comb3 = eval('comb2'+o3+i4)
                                    outputs.add(comb3)
                                except ZeroDivisionError: pass
                                try:
                                    comb3 = eval(i4+o3+'comb2')
                                    outputs.add(comb3)
                                except ZeroDivisionError: pass
                                comb2 = eval(i3+o2+i4)
                                comb3 = eval('comb2'+o3+'comb1')
                                outputs.add(comb3)
                                comb3 = eval('comb1'+o3+'comb2')
                                outputs.add(comb3)

    for i in outputs.copy():
        if i < 1: outputs.remove(i)
        elif type(i) is float:
            outputs.remove(i)
            if i.is_integer() == True:
                outputs.add(int(i))
    n = 0
    while n+1 in outputs:
        n += 1
    return n
for j in range(4,10):
    for k in range(3,j):
        for l in range(2,k):
            for m in range(1,l):
                print(str(m)+str(l)+str(k)+str(j)+': '+str(maxConsec(str(m)+str(l)+str(k)+str(j))))