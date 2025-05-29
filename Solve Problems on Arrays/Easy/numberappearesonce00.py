def Function(arr):
    n = len(arr)
    for i in range(0, n):
        num = arr[i]
        count = 0
        for j in range(0, n):
            if num == arr[j]:
                count += 1
        if count == 1:
            return num
if __name__ == "__main__":
    arr = [1,1,2,2,3,3,5,5,6,6,7,8,8]
    print(Function(arr))
