def recursive_insertion_sort(arr, n):
    # Base case: If the array has one or no elements, it's sorted
    if n <= 1:
        return

    # Recursive call to sort the first n-1 elements
    recursive_insertion_sort(arr, n - 1)

    # Insert the nth element in its correct position
    temp = arr[n - 1]
    j = n - 2
    while j >= 0 and arr[j] > temp:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = temp

# Main function to run the sort
def main():
    array = [5, 4, 10, 1, 6, 2]
    n = len(array)
    recursive_insertion_sort(array, n)
    print(array)

if __name__ == "__main__":
    main()
