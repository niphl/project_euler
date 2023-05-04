def factorial(n):
    prod = 1
    for i in range(1, n+1): prod*= i
    return prod

curiousnums = set()
sum = 0

for i in range(10,9999999):
    prodSum = 0
    for j in str(i):
        prodSum += factorial(int(j))
    if prodSum == i:
        print(i)
        curiousnums.add(i)

for i in curiousnums:
    sum += i
print(sum)

