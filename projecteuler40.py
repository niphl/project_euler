conc = ''
for i in range(200000):
    conc += str(i)
prod = 1
for i in range(7):
    prod *= int(conc[10**i])
print(prod)