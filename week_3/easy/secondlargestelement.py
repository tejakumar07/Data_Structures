# This code is about the second largest element in the list
# This is the Brute Force approach
arr = [12,89,120,98,12,44,1888,1888,1888,1887]
arr.sort()
largest = arr[-1]
n = len(arr)

for i in range(n-2, -1, -1):
    if arr[i] != largest:
        secondlargest = arr[i]
        print(secondlargest)
        break