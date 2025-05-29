
a = [15,16,6,8,5]


n = len(a)

for i in range(0,n-1):
    for j in range(0,n-1):
        if a[j]>a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp

print(a)

#This code is not perfect but solve the Bubble Sort Technique