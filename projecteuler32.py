numbs = '123456789'
"""
for i in range(10):
    it1 = numbs[i:]+numbs[i+1:]
    for j in range(9):
        int(numbs[i])*int(numbs[i:]+numbs[i+1:])
"""
SET, SUM =set(), 0
def pickFive(s, store):
    global SET
    if len(store) == 5:
        newint = int(store[0]+store[1])*int(store[2]+store[3]+store[4])
        for i in str(newint):
            if i == '0': return
            if i in store: return
            if str(newint).count(i) > 1: return
        print('store'+store+'newint'+str(newint))
        SET.add(newint)
        return
    for i in range(len(s)): pickFive(s[:i]+s[i+1:], store+s[i])

def pickFivev2(s, store):
    global SET
    if len(store) == 5:
        newint = int(store[0])*int(store[1]+store[2]+store[3]+store[4])
        for i in str(newint):
            if i == '0': return
            if i in store: return
            if str(newint).count(i) > 1: return
        print('STOREV2'+store+'newint'+str(newint))
        SET.add(newint)
        return
    for i in range(len(s)): pickFivev2(s[:i]+s[i+1:], store+s[i])
k = ''
pickFive(numbs, k)
pickFivev2(numbs, k)

for i in SET:
    SUM += i
print(SET)
print(SUM)