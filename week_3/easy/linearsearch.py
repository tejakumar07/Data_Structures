# This is the Linear Search
def linearSearch(arr,n,num):
    for i in range(0,n):
        if arr[i] == num:
            return "Found"
        
    return "Not Found"
def main():
    arr = list(map(int,input("Array: ").split()))
    n = len(arr)
    num = int(input("Enter Num: "))
    print(linearSearch(arr,n,num))
if __name__ == '__main__':
    main()