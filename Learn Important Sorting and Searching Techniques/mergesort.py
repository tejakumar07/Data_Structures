def merge_array(array,low,mid,high):
    temp = []
    left = low
    right = mid +1
    while left <= mid and right <= high:
        if array[left] <= array[right]:
            temp.append(array[left])
            left+=1
        else:
            temp.append(array[right])
            right += 1
    while left <= mid:
        temp.append(array[left])
        left += 1
    while right <= high:
        temp.append(array[right])
        right += 1
    for i in range(len(temp)):
        array[low+i] = temp[i]
def merge_sort(array,low,high):
    if low >= high:
        return
    mid = (low+high) // 2
    merge_sort(array,low,mid)
    merge_sort(array,mid+1,high)
    merge_array(array,low,mid,high)
def main():
    array = [9,4,7,6,3,1,5]
    n = len(array)
    merge_sort(array,0,n-1)
    print(array)
if __name__ == "__main__":
    main()