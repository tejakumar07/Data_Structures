# Optimum Solution

def reverse(arr,start,end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start +=1
        end -= 1
def lRotate(arr,n):
    d = int(input("D: "))
    d = d % n
    if d == 0:
        return arr
    reverse(arr,0,n-1)
    reverse(arr,0,d-1)
    reverse(arr,d,n-1)
    return arr
def main():
    arr = [1,2,3,4,5,6,7,8,9,10]
    n = len(arr)
    print(f"After Rotating the array: {lRotate(arr,n)}")
if __name__ == "__main__":
    main()