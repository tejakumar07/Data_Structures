import random

a = [random.randint(0,50) for _ in range(0,20)] #It will give you the random numbers in the list 


print(a) #This will print list in unsorted

n = len(a)

for i in range(0,n-1):
    for j in range(0,n-1):
        if a[j]>a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1]=temp

print(a)