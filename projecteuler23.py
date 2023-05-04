def divSum(n):
    sum = 0
    i = 2
    while i**2 < n:
        if n%i == 0: sum += i + n//i
        i += 1
    if i**2 == n: sum += i
    return sum

abundantNums = tuple()
summables = set()
sum = 0
for i in range(12,28123):
    if divSum(i) > i: abundantNums += i,
for i in abundantNums:
    for j in abundantNums: summables.add(i + j)
print(abundantNums)
print(summables)
for i in range(1,28124):
    if i not in summables: sum += i
print(sum)