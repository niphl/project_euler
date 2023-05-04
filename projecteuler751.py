x = '2.223561019313554106173177'
tuple = (2, 3)
b = float(x+'0000')
iterations = 0
while iterations <= 15:
    b = (b//1)*(b-(b//1)+1)
    a = int(b // 1)
    iterations += 1
    tuple += a,
    print(a)
print(x)
