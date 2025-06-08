# Type -I 
# Optimal Approach

def ArrangeTheElementsBySign(nums):
    ans = [0] * len(nums)
    postive = 0
    negative = 1
    for num in nums:
        if num < 0:
            ans[negative] = num
            negative += 2
        else:
            ans[postive] = num
            postive += 2
    return ans

if __name__ == "__main__":
    nums = [3,1,-2,-5,2,-4]
    print(ArrangeTheElementsBySign(nums))