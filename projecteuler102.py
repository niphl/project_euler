
#We write a function that takes a tuple of 6 inputs, and outputs whether or not the origin is in the triangle
l = tuple()
with open('p102_triangles.txt', 'r') as f:
    for line in f:
        l += tuple(map(int, line.split(','))),
print(l)
print(len(l))
import cmath
def originCheck(t):
    a, b, c = complex(t[0], t[1]), complex(t[2], t[3]), complex(t[4], t[5])
    p, q, r = cmath.phase(a/b), cmath.phase(b/c), cmath.phase(c/a)
    #print(str(cmath.phase(a))+','+str(cmath.phase(b))+','+str(cmath.phase(c)))
    #print(str(p) + ',' + str(q) + ',' + str(r))
    if p > 0 and q > 0 and r > 0: return 1
    elif p < 0 and q < 0 and r < 0: return 1
    else: return 0

sum = 0
for i in l:
    sum += originCheck(i)

print(sum)
