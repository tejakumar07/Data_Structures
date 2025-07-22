# Brute Force Approach
# Using Linear Search

def search_in_sorted_array(nums, X):
    n = len(nums)
    
    for i in range(n):
        if nums[i] == X:
            return i
    return -1

if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    target = 0
    ans =search_in_sorted_array(nums, target)
    print(ans)