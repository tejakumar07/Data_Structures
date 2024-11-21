#This is another  pattern
"""
A
BB
CCC
DDDD
EEEEE

"""
n=6
num = 65

for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(num),end="")      
    print("")
    num+=1