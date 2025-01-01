# Left Rotate Array 'D' Places
def leftRotate(arr,n):
    # Coping the First Element in the Array
    temp = arr[0]
    for i in range(1,n):
        # Moving the Array Elements to Back
        arr[i-1] = arr[i]
    # Adding the First Element to Last
    arr[n-1] = temp
    return arr
def main():
    # Taking Input
    arr = list(map(int,input("List: ").split()))
    # Printing the Array Entered
    print(f"The Entered List is: {arr}")
    # Finding the Length of the Array
    n = len(arr)
    # Calling the Function
    print(f"After Left Rotating '1' Place {leftRotate(arr,n)}")
if __name__ == "__main__":
    main()
