def factorial(a):
    prod = 1
    for i in range(1,a+1):
        prod *= i
    return prod
def prodRange(start, stop):
    prod = 1
    for i in range(start+1, stop):
        prod *= i
    return prod

ways = 0
r, g, b = 0,0,0
while 50-2*r-3*g-4*b > -1:
    while 50 - 2 * r - 3 * g - 4 * b > -1:
        while 50-2*r-3*g-4*b > -1:
            ways += factorial(50-r-2*g-3*b)//(factorial(50-2*r-3*g-4*b)*factorial(r)*factorial(g)*factorial(b))
            r += 1
            print(ways)
        g += 1
        r = 0
    b += 1
    g = 0
    r = 0
print(ways)