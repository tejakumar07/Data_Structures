class Solution:
    def nCr(self, n, r):
        if n < 0 or r < 0:
            return
        if r > n:
            return 0
        result = 1
        for i in range(r):
            result *= n - i
            result //= i + 1
        return result
    def PrintingTriangle(self, n):
        ans = []
        for row in range(n):
            templist  = []
            for col in range(row + 1):
                templist.append(self.nCr(row, col))
            ans.append(templist)
        return ans

if __name__ == "__main__":
    teja = Solution()
    print(teja.PrintingTriangle(3))