k = 10**10
def rPowmk(a,b):
    count = 0
    num = 1
    while count < b:
        num *= a
        num %= k
        count += 1
    return num
sum = 0
for i in range(1,1001):
    sum += rPowmk(i,i)
    sum %= k
print(sum)