l = (319, 680, 180, 690, 129, 620, 762, 689, 762, 318, 368, 710, 720, 710, 629, 168, 160, 689, 716, 731, 736, 729, 316, 729, 729, 710, 769, 290, 719, 680, 318, 389, 162, 289, 162, 718, 729, 319, 790, 680, 890, 362, 319, 760, 316, 729, 380, 319, 728, 716)
t = tuple()
password = '73162890'

for g in l:
    i = str(g)
    if password.index(i[0]) == -1 or password.index(i[1]) == -1 or password.index(i[2]) == -1:
        print(i+' not found in password.')
    if password.index(i[0]) > password.index(i[1]) or password.index(i[1]) > password.index(i[2]):
        print(i+' not in correct order in password.')
    else: print(i+' found successfully')


