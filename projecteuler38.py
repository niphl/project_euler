ints = '123456789'
num = 9
def pandigital(j):
    i = 1
    concproduct = ''
    num = int('9'+str(j))
    while len(concproduct+str(num*i)) < 10:
        concproduct += str(num*i)
        i += 1
    for i in range(9):
        if concproduct.count(ints[i]) != 1:
            return
    if '0' in concproduct:
        return
    print(concproduct)

for j in range(1000):
    pandigital(j)