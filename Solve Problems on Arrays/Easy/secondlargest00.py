# Brute Force Approah
def SecondLargest(arr):
    arr.sort()
    largest = arr[-1]
    for i in range(len(arr)-2, 0, -1):
        if arr[i] != largest:
            slargest = arr[i]
            return slargest

if __name__ == "__main__":
    arr = list(map(int, input("Array: ").split()))
    print(SecondLargest(arr))
