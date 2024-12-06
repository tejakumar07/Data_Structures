def bubble_sort(list,size):
    for i in range(size-1):
        swapped = False
        for j in range(0,size-i-1):
            if list[j] > list[j+1]:
                list[j+1], list[j] = list[j], list[j+1]
                swapped = True
        if not swapped:
            break
    return list
def main():
    array = list(map(int,input("List: ").split()))
    n = len(array)
    print(bubble_sort(array,n))
if __name__ == "__main__":
    main()