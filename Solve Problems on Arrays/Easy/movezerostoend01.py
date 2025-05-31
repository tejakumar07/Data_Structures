# Optimal Solution
def pushZerosAtEnd(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j+=1
    return arr
        


if __name__ == "__main__":
    arr = [1,2,0,0,3,0,0,4,0,0,5,0,0,6,0,7,0,0,0,8]
    print(pushZerosAtEnd(arr))
