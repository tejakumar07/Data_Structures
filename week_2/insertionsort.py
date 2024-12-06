array = [5,4,10,1,6,2]
n = len(array)

for i in range(n):
    temp= array[i]
    j = i - 1
    while(j >= 0 and array[j] > temp):
        array[j+1] = array[j]
        j -= 1
    array[j+1] = temp

print(array)
