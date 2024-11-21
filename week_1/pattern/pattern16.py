#This is another Pattern

"""
      A
     ABA
    ABCBA
   ABCDCBA
  ABCDEDCBA

"""

num = 65
n=6

for i in range(1,n+1):
    for j in range(n,i,-1):
        print("",end="")
    for j in range(1,2*i-1):
        print("*",end="")
    for j in range(n,1,-1):
        print("",end="")
    print("")
    