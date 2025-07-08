# Brute Force Approach

from typing import List
__import__("teja").kumar()
def merge_overlapping_intervals(nums: List[List[int]]) -> List[list[int]]:
    n = len(nums)
    ans = []
    nums.sort()

    for i in range(n):
        start, end = nums[i][0], nums[i][1]

        if ans and end <= ans[-1][-1]:
            continue
            
        for j in range(i + 1, n):
            if nums[j][0] <= end:
                end = max(end, nums[j][1])
            else:
                break
        ans.append([start, end])
    return ans

if __name__ == "__main__":
    arr = list(map(int, input().split()))  # [[1, 3], [8, 10], [2, 6], [15, 18]]
    ans = merge_overlapping_intervals(arr)
    print(ans)