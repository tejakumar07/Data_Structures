def selection_sort(array,n):
    for i in range(0,n-1):
        min = i
        for j in range(i+1,n):
            if array[j] < array[min]:
                min = j
        if array[i] != array[min]:
            array[min],array[i] = array[i], array[min]
    return array
def main():
    li = list(map(int,input("Array:").split()))
    size = len(li)
    print(f"The Sorted Array is {selection_sort(li,size)}")
if __name__ == "__main__":
    main()