a = [7, 4, 10, 8, 3, 1]  # Initialize the array to be sorted

n = len(a)  # Get the length of the array

# Outer loop: Iterate through each element of the array (except the last one)
for i in range(0, n - 1):
    min = i  # Assume the smallest element is at the current index i

    # Inner loop: Find the smallest element in the unsorted part of the array
    for j in range(i + 1, n):  # Compare the current element with the rest
        if a[j] < a[min]:  # Check if the element at index j is smaller than the current minimum
            min = j  # Update min to the index of the smaller element

    # Swap the smallest element with the first element of the unsorted part
    if a[i] != a[min]:  # Check if the smallest element is not already in the correct position
        a[i], a[min] = a[min], a[i]  # Perform the swap

print(a)  # Print the sorted array
