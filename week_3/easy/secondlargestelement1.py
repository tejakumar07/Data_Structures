# This is the Better Approach
def secondLargestElement(arr,n,largest_element):
    second_largest_element = float('-inf')
    for i in range(n):
        if arr[i] > second_largest_element and arr[i] < largest_element:
            second_largest_element = arr[i]
    return second_largest_element
def largestElement(arr,n):
    largest_element = arr[0]
    for i in range(n):
        if arr[i] > largest_element:
            largest_element = arr[i]
    return largest_element
def main():
    array = [1,2,4,7,7,5]
    size = len(array)
    largest = largestElement(array,size)
    print(f"The Second Largest Element is: {secondLargestElement(array,size,largest)}")
if __name__ == "__main__":
    main()
