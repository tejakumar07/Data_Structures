# This is the Type - 2 Problem
# Brute Force Approach


class Solution:
    def nCr(self, n, r):
        if n < 0 or r < 0:
            return
        if r > n:
            return 0
        result = 1
        for i in range(r):
            result *= (n - i)
            result //= i+1
        return result
    def getRow(self, n):
        temp = []
        for c in range(n +1):
            temp.append(self.nCr(n, c))
        return temp

if __name__ == "__main__":
    teja = Solution()
    print(teja.getRow(3))