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
#red tiles
r, g, b = 1,1,1
while 50-2*r > -1:
    ways += prodRange(r, 51-r)//factorial(50-2*r)
    r += 1
    #print('r', r, ways)
while 50-3*g > -1:
    ways += prodRange(g, 51-2*g)//factorial(50-3*g)
    g += 1
    #print('g', g, ways)
while 50-4*b > -1:
    ways += prodRange(b, 51-3*b)//factorial(50-4*b)
    b += 1
    #print('b', b, ways)
print(ways)