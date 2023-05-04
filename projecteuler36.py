print(bin(585)[2:])
def isPalindromeDouble(a):
    b = bin(a)[2:]
    a = str(a)
    for i in range(len(a)//2):
        if a[i] != a[len(a)-1-i]: return 0
    for i in range(len(b)//2):
        if b[i] != b[len(b)-1-i]: return 0
    return 1

sum = 0
for i in range(10**6+1):
    if isPalindromeDouble(i) == 1:
        print(i)
        sum += i
print(sum)