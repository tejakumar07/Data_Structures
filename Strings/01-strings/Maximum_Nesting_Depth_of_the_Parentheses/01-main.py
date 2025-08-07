class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        maxi = 0
        for ch in s:
            if ch == "(":
                count += 1
            elif ch == ")":
                count -= 1
            else:
                continue
            maxi = max(maxi, count)
        return maxi

if __name__ == "__main__":
    teja = Solution()
    s = "(1+(2*3)+((8)/4))+1"
    print(teja.maxDepth(s))