#This is another Pattern
"""
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********

"""

n = 6

# This is for the Upper Symmetry
for i in range(0,n):
    # This is For the Stars
    for j in range(0,n-i):
        print("*",end="")
    # This is for the Spaces
    for j in range(0,2*i):
        print(" ",end="")
    # This is again For the Stars
    for j in range(0,n-i):
        print("*",end="")
    print("")

# This is Lower Symmetry
for i in range(0,n):
    # This is for the Star
    for j in range(0,i+1):
        print("*",end="")
    # This is for the Spaces
    for j in range(0,(2*n)-(2*(i+1))):
        print(" ",end="")
        
    # Again this is for the Stars
    for j in range(0,i+1):
        print("*",end="")
    print("")
