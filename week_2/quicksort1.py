def merge(arr, low, mid, high):
    # Using slices to simplify merging
    left_part = arr[low:mid+1]
    right_part = arr[mid+1:high+1]

    left_index, right_index, merged_index = 0, 0, low

    # Merge the two parts
    while left_index < len(left_part) and right_index < len(right_part):
        if left_part[left_index] <= right_part[right_index]:
            arr[merged_index] = left_part[left_index]
            left_index += 1
        else:
            arr[merged_index] = right_part[right_index]
            right_index += 1
        merged_index += 1

    # Append remaining elements from the left part
    arr[merged_index:merged_index + len(left_part[left_index:])] = left_part[left_index:]

    # Append remaining elements from the right part
    arr[merged_index + len(left_part[left_index:]):] = right_part[right_index:]

def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)

def main():
    arr = list(map(int, input("Enter the array (space-separated): ").split()))
    print(f"Original Array: {arr}")
    merge_sort(arr, 0, len(arr) - 1)
    print(f"Sorted Array: {arr}")

if __name__ == "__main__":
    main()