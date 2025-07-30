# Optimal approach

class Solution:
    def lowerBound(self, nums):
        n = len(nums)
        ans = n
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] >= 1:
                high = mid - 1
                ans = mid
            else:
                low = mid + 1
        return ans
    def rowAndMaximumOnes(self, mat):
        n = len(mat)
        maxRow = 0
        maxIndx = -1
        m = len(mat[0])
        for i in range(n):
            rowCount = m - self.lowerBound(mat[i])

            if rowCount > maxRow:
                maxRow = rowCount
                maxIndx = i
        return [maxIndx, maxRow]
    
if __name__ == "__main__":
    mat = [[0,1],[0,0], [1,1]]
    sol = Solution()
    ans = sol.rowAndMaximumOnes(mat)
    print(ans)