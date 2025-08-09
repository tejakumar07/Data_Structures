class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest = ''

        for i in range(n):
            for j in range(i, n):
                substring = s[i: j + 1]
                if substring == substring[::-1] and len(substring) > len(longest):
                    longest = substring
        return longest

s = "babad"
teja = Solution()
print(teja.longestPalindrome(s))