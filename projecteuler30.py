def digitpsum(n):
    strn = str(n)
    sum=0
    for i in range(len(strn)):
        sum+=int(strn[i])**5
    return sum
sum = 0
for i in range(300000):
    if digitpsum(i) == i:
        sum += i
        print(i)
print(sum)