#This is similar to last pattern
"""
    *     [3,1,3]
   ***    [2,3,2]
  *****   [1,5,1]
 *******  [0,7,0] 
 *******  [0,7,0]
  *****   [1,5,1]
   ***    [2,3,2]
    *     [3,1,3]
"""

n = int(input("What's N: "))

#For First Pattern
for i in range(0,n):
    for j in range(0,n-i-1):
        print(" ",end="")
    for j in range(0,2*i+1):
        print("*",end="")
    for j in range(0,n-i-1):
        print("",end="")
    print("")


#This is for 2nd Pattern
for i in range(0,n):
    for j in range(0,i):
        print(" ",end="")
    for j in range(0,2*n-(2*i+1)):
        print("*",end="")
    for j in range(0,i):
        print("",end="")
    print("")