#This is another Pattern
"""

*
**
***
****
*****
****
***
**
*

"""

n = int(input("What's N: "))

for i in range(0,n):
    for j in range(0,i+1):
        print("*",end="")
    print("")

for i in range(0,n):
    for j in range(0,n-1-i):
        print("*",end="")
    print("")