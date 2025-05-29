def LeftRotateArrayByDPlaces(arr, d):
    n = len(arr)
    d = d % n
    return arr[d:] + arr[:d]

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    d = int(input("D: "))
    rotated_arr = LeftRotateArrayByDPlaces(arr, d)
    print(rotated_arr)
