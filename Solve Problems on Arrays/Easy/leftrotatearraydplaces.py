def LeftRotateArrayByDPlaces(arr, d):
    n = len(arr)
    d = d % n
    temp = []
    for i in range(d):
        temp.append(arr[i])
    for i in range(d, n):
        arr[i-d] = arr[i]
    low = 0
    for i in range(n-d, n):
        arr[i] = temp[low]
        low += 1
    print(f"After Rotating the Array: {arr}")

if __name__ == "__main__":
    arr = [x for x in map(int, input("Array: ").split())]
    print(f"Before Rotating the Array: {arr}")
    d = int(input("D: "))
    LeftRotateArrayByDPlaces(arr, d)
