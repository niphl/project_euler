def factorial(n):
    prod = 1
    for i in range(1, n+1): prod*= i
    return prod
print(factorial(10))

t = tuple('0123456789')
t_test = tuple('012')

def permute(t, num, stored):
    numstemp = t
    if len(t) == 1: print(stored+str(t[0]))
    else:
        i, j = num//factorial(len(t)-1), num%factorial(len(t)-1)
        newt = (numstemp[i], ) + numstemp[:i] + numstemp[i + 1:]
        stored += str(newt[0])
        return permute(newt[1:], j, stored)

print(permute(t, 10**6-1,'stored'))
