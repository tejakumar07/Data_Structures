def LeftRotateArrayByDPlaces(arr, d):
    n = len(arr)
    d = d % n
    Reverse(arr, 0, d - 1)
    Reverse(arr, d, n - 1)
    Reverse(arr, 0, n - 1)

def Reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

if __name__ == "__main__":
    arr = [x for x in map(int, input("Array: ").split())]
    d = int(input("D: "))
    LeftRotateArrayByDPlaces(arr, d)
    print(arr)
