def insertion_sort(a,n):
    for i in range(1,n):
        temp = a[i]
        j = i - 1
        while(j >= 0 and a[j] > temp):
            a[j+1] = a[j]
            j -= 1
        a[j+1] = temp
    return a
def main():
    array = list(map(int,input("Array: ").split()))
    size = len(array)
    print(f"The Sorted array is {insertion_sort(array,size)}")
if __name__ == "__main__":
    main()