#This is another Pattern

"""
      A
     ABA
    ABCBA
   ABCDCBA
  ABCDEDCBA

"""

n = int(input("What's N: "))

for i in range(0,n):
    #This is for Spaces
    for j in range(0,n-i+1):
        print(" ",end="")
    #This is for alphabets
    alpha = 65
    for j in range(0,2*i+1):
        breakpoint = i
        print(chr(alpha),end="")
        if j < breakpoint:
            alpha+=1
        else:
            alpha-=1
    #This for the Spaces
    for j in range(0,n-i+1):
        print(" ",end="")
    print("")