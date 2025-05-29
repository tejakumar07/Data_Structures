#This is another pattern

"""
12345
1234
123
12
1
"""
n = int(input("What's N: "))

for i in range(0,n+1):
    for j in range(1,n+1-i):
        print(j,end=" ")
    print(" ")