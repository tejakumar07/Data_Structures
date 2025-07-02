__import__("teja").kumar()

def threeSum(nums):
    n = len(nums)
    nums.sort()
    ans = []

    for i in range(n):
        if i != 0 and nums[i] == nums[i-1]:
            continue
        
        j = i + 1
        k = n - 1

        while j < k:
            total_sum = nums[i] + nums[j] + nums[k]

            if total_sum < 0:
                j += 1
            elif total_sum > 0:
                k -= 1
            else:
                ans.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1

                while j < k and nums[j] == nums[j-1]:
                    j += 1
                while j < k and nums[k] == nums[k+1]:
                    k -= 1

    return ans

if __name__ == "__main__":
    nums = list(map(int, input().split())) # nums = [-1,0,1,2,-1,-4]
    print(threeSum(nums))