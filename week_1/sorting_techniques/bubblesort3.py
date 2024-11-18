import random
import time



a = [random.randint(0,100000) for _ in range(0,10)]

n = len(a)
print(a)
print(n)

#Starting the time Here

start_time = time.time()

for i in range(0,n-1):
    for j in range(0,n-1-i):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j]=a[j+1]
            a[j+1]=temp

end_time = time.time()

print(a) #this will print sorted list

total_time = end_time - start_time

print("The Time taken is to complete is: ",total_time)