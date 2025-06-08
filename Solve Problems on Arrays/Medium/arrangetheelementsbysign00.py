# Type - I
# LeetCode Style Elements are equal (i.e both +ve and -ve)

# Brute Foce Approach

def ArrangeTheElementsBySign(nums):
    postive = []
    negative = []
    
    for num in nums:
        if num > 0:
            postive.append(num)
        else:
            negative.append(num)
    
    for i in range(len(nums)//2):
        nums[i*2] = postive[i]
        nums[i*2+1] = negative[i]
    return nums

if __name__ == "__main__":
    nums = [3,1,-2,-5,2,-4]
    print(ArrangeTheElementsBySign(nums))