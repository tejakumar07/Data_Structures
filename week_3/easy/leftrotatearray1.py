def lRotate(arr,n):
    d = int(input("D: "))
    d = d % n
    if d == 0:
        return arr
    temp = []
    for i in range(0,d):
        temp.append(arr[i])
    for i in range(d,n):
        arr[i-d] = arr[i]
    for i in range(n-d,n):
        arr[i] = temp[i-(n-d)]
    return arr
def main():
    arr = [1,2,3,4,5,6,7,9]
    n = len(arr)
    print(f"After Rotating the array: {lRotate(arr,n)}")
if __name__ == "__main__":
    main()