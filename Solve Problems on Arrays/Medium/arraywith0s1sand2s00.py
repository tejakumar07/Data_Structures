# Brute Force Approach

def SortingZerosOncesAndTwos(nums):
    from collections import Counter
    n = len(nums)
    count_0 = arr.count(0)
    count_1 = arr.count(1)
    count_2 = arr.count(2)
    
    for i in range(0, count_0):
        arr[i] = 0
    for i in range(count_0, count_0 + count_1):
        arr[i] = 1
    for i in range(count_0 + count_1, count_0+count_1+count_2):
        arr[i] = 2
    return arr

if __name__ == "__main__":
    arr = [0,1,2,0,1,2,1,2,0,0,0,1]
    print(SortingZerosOncesAndTwos(arr))