def recursive_bubble_sort(arr, n):
    # Base case: if the size is 1 or less, it's already sorted
    if n == 1:
        return

    # One pass of Bubble Sort (same as the inner loop of Bubble Sort)
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    # Recursive call for the next pass
    recursive_bubble_sort(arr, n - 1)

# Main function to run the sort
def main():
    array = [4, 1, 5, 2, 9, 16]
    n = len(array)
    recursive_bubble_sort(array, n)
    print(array)

if __name__ == "__main__":
    main()
