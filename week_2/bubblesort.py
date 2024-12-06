array = [4,1,5,2,9,16]
n = len(array)

for i in range(1,n-1):
    swapped = False
    for j in range(0,n-i-1):
        if array[j] > array[j+1]:
            array[j+1] , array[j] = array[j], array[j+1]
            swapped = True
    if not swapped:
        break

print(array)