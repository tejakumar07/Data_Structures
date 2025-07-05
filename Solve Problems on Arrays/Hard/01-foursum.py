# Brute Force Approach
__import__("teja").kumar()

def four_sum(nums, target):
    n = len(nums)
    st = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        temp = [nums[i], nums[j], nums[k], nums[l]]
                        temp.sort()
                        st.add(tuple(temp))
    ans = [list(item) for item in st]
    return ans

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    target = int(input())
    print(four_sum(arr, target))