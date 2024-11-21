#This is another patttern
"""
A
AB
ABC
ABCD

"""

n = int(input("what's N: "))

for i in range(1,n+1):
    num=65
    for j in range(1,i+1):
        print(chr(num),end="")
        num+=1
    print("")
