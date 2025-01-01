# This code is about the second largest element in the list
# This is the Brute Force approach

arr = [2,4,1,5,7,7,10,10]
n = len(arr)
largest_element = arr[n-1]

for i in range(n-2,0,-1):
    if largest_element != arr[i]:
        second_largest = arr[i]
        break
print(f"The Second Largest Element is: {second_largest}")