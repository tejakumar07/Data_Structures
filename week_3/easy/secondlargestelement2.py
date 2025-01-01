# This is the Optimum approach
def main():
    arr = list(map(int,input("Array: ").split()))
    print(f"The List Enterd is: {arr}")
    n = len(arr)
    print(f"The Largest and Second Largest Elements are: {slargest(arr,n)}")
def slargest(arr,n):
    largest = arr[0]
    second_largest = float('-inf')
    for i in range(n):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif  arr[i] < largest and arr[i] > second_largest:
            second_largest = arr[i]
    return largest,second_largest
if __name__ == "__main__":
    main()