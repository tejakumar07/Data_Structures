# Brute Force Approach
# Using Linear Search

from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        for i in range(n):
            if arr[i] <= k:
                k += 1
            else:
                break
        return k

if __name__ == "__main__":
    teja = Solution()
    arr = [2,3,4,7,11]
    k = 5
    ans = teja.findKthPositive(arr, k)
    print(ans)