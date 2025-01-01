def maximumElement(arr,length):
    # Taking that 1st element as largest element
    maximum = arr[0]
    # Comparing the element with all the elements in the list
    for i in range(length):
        # if any element larger that the maximum element then updating the maximum element
        if arr[i] > maximum:
            maximum = arr[i]
    return maximum
def main():
    # Taking Input List from the user
    array = list(map(int,input("Enter the List: ").split()))
    # Finding the Length of the List
    size = len(array)
    # Calling the Function and Print the largest value
    print(f"The Largest Element in the List is: {maximumElement(array,size)}")
if __name__ == "__main__":
    main()