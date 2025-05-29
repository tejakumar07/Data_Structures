# Optimal Approach

def Function(nums):
    xor1 = 0
    for num in nums:
        xor1 ^= num
    return xor1

if __name__ == "__main__":
    arr = [1,1,2,2,3,3,5,5,6,6,7,8,8]
    print(Function(arr))
