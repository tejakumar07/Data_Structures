#This is another pattern

"""
    *
   ***
  *****
 *******  
"""

n = int(input("What's N: "))

for i in range(0,n):
    for j in range(0,n-i-1):
        print(" ",end="")
    for j in range(0,2*i+1):
        print("*",end="")
    print(" ")

#This can also be done using 
"""
for i in range(0,n):
    for j in range(0,n-i-1):
        print(" ",end="")
    for j in range(0,2*i+1):
        print("*",end="")
    for j in range(0,n-i-1):
        print("",end="")
    print("")
"""


