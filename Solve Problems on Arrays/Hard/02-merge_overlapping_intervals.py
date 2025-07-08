# Optimal Approach
from typing import List

__import__("teja").kumar()
def merge_overlapping_intervals(nums: List[List[int]]) -> List[List[int]]:
    n = len(nums)
    ans = []
    nums.sort()

    for i in range(n):
        if not ans or ans[-1][-1] < nums[i][0]:
            ans.append(nums[i])
        else:
            ans[-1][-1] = max(ans[-1][-1], nums[i][1])
    return ans

if __name__ == "__main__":
    arr = list(map(int, input().split())) # [[1, 3], [8, 10], [2, 6], [15, 18]]
    ans = merge_overlapping_intervals(arr)
    print(ans)