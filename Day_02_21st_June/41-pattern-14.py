'''
A
AB
ABC
ABCD
ABCDE
'''

for i in range(6):
    a=65
    for j in range(i):
        print("%c"%(a),end='')
        a+=1
    print()