#This is another pattern
'''
E
DE
CDE
BCDE
ABCDE

'''

n=int(input("What's N: "))
for i in range(0,n):
    alpha = 69-i
    for j in range(0,i+1):
        print(chr(alpha),end="")
        alpha+=1
    print("")