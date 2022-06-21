'''
4321
321
21
1
'''

rows = 4
for i in range(rows):
    for j in range(rows - i, 0, -1):
        print(j, end='')
    print()