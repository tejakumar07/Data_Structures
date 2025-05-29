# This is another Pattern
'''
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
'''


n = int(input("what's N: "))

# This is for the First Symmetry
for i in range(1, n+1):
    for j in range(0, i):
        print("*", end="")
    for j in range(0, 2 * (n - i)):
        print(" ", end="")
    for j in range(0, i):
        print("*", end="")
    print("")

# This is for the Secondary Symmetry

for i in range(n,0,-1):
    for j in range(0,i):
        print("*",end="")
    for j in range(0,2*(n-i)):
        print(" ",end="")
    for j in range(0,i):
        print("*",end="")
    print("")