def TwoSum(nums, k):
    nums.sort()
    i = 0
    j = len(nums)-1
    
    while i < j:
        if nums[i] + nums[j] == k:
            return "Yes"
        elif nums[i] + nums[j] < k:
            i+=1
        else:
            j-=1
    return "NO"

if __name__ == "__main__":
    arr = [1,4,9,14,8,10,3,7]
    target = 22
    print(TwoSum(arr, target))