def LinearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
if __name__ == "__main__":
    arr = [x for x in map(int, input("Array: ").split())]
    print(f"The Entered Array is: {arr}")
    target = int(input("Target: "))
    print(LinearSearch(arr, target))
