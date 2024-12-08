def partition(arr, low, high):
    # Choose the first element as the pivot
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        # Move `i` to the right until an element greater than the pivot is found
        while arr[i] <= pivot and i < high:
            i += 1
        # Move `j` to the left until an element less than or equal to the pivot is found
        while arr[j] > pivot and j > low:
            j -= 1
        # Swap elements at i and j if they have not crossed each other
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # Swap the pivot with the element at index j
    arr[low], arr[j] = arr[j], arr[low]
    return j  # Return the partition index

def quick_sort(arr, low, high):
    if low < high:
        # Partition the array and get the partition index
        pIndex = partition(arr, low, high)
        # Recursively sort the elements before and after the partition
        quick_sort(arr, low, pIndex - 1)
        quick_sort(arr, pIndex + 1, high)

def main():
    array = [4, 6, 2, 5, 7, 9, 1, 3]
    n = len(array)
    quick_sort(array, 0, n - 1)
    print("Sorted array:", array)  # Print the sorted array

if __name__ == "__main__":
    main()
