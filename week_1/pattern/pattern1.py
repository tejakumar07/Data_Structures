#In this let's try another pattern
"""
*
**
***
****

"""

n = int(input("What's N: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print("")