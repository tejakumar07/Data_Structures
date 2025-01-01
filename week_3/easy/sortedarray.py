# This is the Stright Forward Q/n

def main():
    arr = list(map(int,input("Enter the Array: ").split()))
    n = len(arr)
    print(checkSorted(arr,n))
def checkSorted(arr,n):
    if n == 1:
        return True
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            return False
    return True
if __name__ == "__main__":
    main()