array = [7,4,10,8,3,1]
n = len(array)

for i in range(0,n-1):
    min = i
    for j in range(i+1,n):
        if array[j] < array[min]:
            min = j
    if array[min] != array[i]:
        array[i], array[min] = array[min], array[i]

print(array)