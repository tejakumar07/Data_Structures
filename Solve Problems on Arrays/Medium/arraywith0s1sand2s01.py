# Optimal Solution
# Using the Dutch National Flag Algorithm

def SortingZerosOncesAndTwos(nums):
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            mid+=1
            low+=1
        elif nums[mid] == 1:
            mid+=1
        elif nums[mid] == 2:
            nums[mid], nums[high] = nums[high], nums[mid]
            high-=1
    return nums
if __name__ == "__main__":
    arr = [0,1,2,0,1,2,1,2,0,0,0,1]
    print(SortingZerosOncesAndTwos(arr))