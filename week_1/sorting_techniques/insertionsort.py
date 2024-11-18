a = [5, 4, 10, 1, 6, 2]  # List to be sorted

n = len(a)

for i in range(1, n):  # Start from the second element (index 1)
    temp = a[i]         # Store the current element
    j = i - 1           # Compare with elements on the left
    while j >= 0 and a[j] > temp:  # Shift elements that are greater than temp
        a[j + 1] = a[j]  # Move element to the right
        j -= 1

    a[j + 1] = temp  # Insert the element at the correct position

print(a)  # Final sorted list
