# This is the Optimum Solution
# For Moving Zeroes to the End.

def movingZeroes(arr,n):
    j = -1
    for i in range(0,n):
        if arr[i] == 0:
            j =i
            break
    for i in range(j+1,n):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return arr
def main():
    arr = list(map(int,input("Enter the List with Zeroes: ").split()))
    print(f'The Entered List is: {arr}')
    n = len(arr)
    print(f"Printing the Array after moving Zeroes: {movingZeroes(arr,n)}")
if __name__ == "__main__":
    main()