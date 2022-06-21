'''
ABCDE
ABCD
ABC
AB
A
'''

for i in range(6,1,-1):
    a=65
    for j in range(1,i):
        print("%c"%(a),end='')
        a+=1
    print()