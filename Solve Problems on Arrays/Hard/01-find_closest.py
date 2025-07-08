__import__('teja').kumar()

def find_closet(nums, k):
    closest = nums[0]
    mini_diff = abs(k - closest)

    for num in nums[1:]:
        diff = abs(k - num)
        if diff < mini_diff:
            mini_diff = diff
            closest = num
    return closest

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    target = int(input())
    print(find_closet(arr, target))