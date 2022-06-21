'''
1
23
456
78910
'''

r=4
c=1
for i in range(r+1):
    for j in range(1,i+1):
        print(c,end="")
        c=c+1
    print()