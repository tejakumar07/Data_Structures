n1 = int(input("What's N1: "))
n2 = int(input("What's N2: "))

num = min(n1,n2)

for i in range(num,1,-1):
    if (n1%i==0 and n2%i==0):
        print(i)
        break