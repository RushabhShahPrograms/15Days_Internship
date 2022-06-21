'''
ABCDE
BCDE
CDE
DE
E
'''

for i in range(0, 5):
    for j in range(65+i, 70):
        a = chr(j)
        print(a, end="")
    print()