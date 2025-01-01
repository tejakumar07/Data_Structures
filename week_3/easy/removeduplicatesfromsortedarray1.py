# Optimum Solution
# Only Works For Sorted array
def removingDuplicatElements(arr,n):
    i = 0
    for j in range(0,n):
        if arr[i] != arr[j]:
            arr[i+1] = arr[j]
            i += 1
    unique_elements = arr[:i+1]
    return unique_elements
def main():
    arr = list(map(int,input("List: ").split()))
    print(f"The Entered List is: {arr}")
    n = len(arr)
    print(f"After Removing Duplicate Elements: {removingDuplicatElements(arr,n)}")
if __name__ == "__main__":
    main()