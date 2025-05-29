#This is reverse pattern for the last code
"""

*******
 *****
 ***
  *

"""
n= int(input("What's N: "))
for i in range(0,n):
    #This is for Spaces
    for j in range(0,i):
        #This is for Stars
        print(" ",end=" ")
    for j in range(0,2*n-(2*i+1)):
            print("*",end=" ")
    #Again this is for Space
    for j in range(0,i):
        print(" ",end=" ")

    print("")

