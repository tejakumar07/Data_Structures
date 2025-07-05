__import__("teja").kumar()

def four_sum(nums, target):
    nums.sort()
    n = len(nums)
    st = set()

    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            seen = set()
            for k in range(j + 1, n):
                fourth = target - nums[i] - nums[j] - nums[k]
                if fourth in seen:
                    quad = tuple(sorted([nums[i], nums[j], nums[k], fourth]))
                    st.add(quad)
                seen.add(nums[k])
    
    return [list(item) for item in st]

if __name__ == "__main__":
    arr = list(map(int, input("Array: ").split()))
    target = int(input("Target: "))
    print(four_sum(arr, target))
