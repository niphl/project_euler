def intAreaM1(a): #c will be a-1, triangle side legnths will be 2a+1, 2a+1, 2a
    s = 3a+1
    #Heron formula (3a+1)(a)(a)(a+1)
    """if isSquare((a+c//2)*(c//2)*(c//2)*(a-c//2)) == 1: return 1""" #Factor out C//2
    if isSquare((3a+1)*(a+1)) == 1: return 1
    else: return 0

def intAreaP1(a): #c will be a-1, triangle side length will be 2a+1, 2a+1, 2a+2
    s = 3a+2
    #Heron formula (3a+2)(a)(a)(a)
    """if isSquare((a+c//2)*(c//2)*(c//2)*(a-c//2)) == 1: return 1""" #Factor out C//2
    if isSquare((3a+2)*a) == 1: return 1
    else: return 0

def isSquare(num):
    #We use newton-raphson to get an approximate square root
    if num == 1: return 1
    x = num / 2
    lastroot = 0
    iterations = 0
    while abs(x - lastroot) > 1:
        lastroot = x
        x = x / 2 + num / (2 * x)
        iterations += 1
    if (x//1)**2 == num or ((x//1)+1)**2 == num: return 1
    else: return 0

print(isSquare(11))
print(intAreaM1)