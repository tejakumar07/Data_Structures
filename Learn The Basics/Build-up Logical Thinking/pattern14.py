#This is inverted pattern for the last pattern

"""

ABCDE
ABCD
ABC
AB
A

"""

n= int(input("What's N: "))

for i in range(n,1,-1):
    num = 65
    for j in range(1,i):
        print(chr(num),end="")
        num+=1
    print("")