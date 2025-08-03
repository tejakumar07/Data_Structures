class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)

if __name__ == "__main__":
    sol = Solution()

    s = "anagram"
    t = "nagaram"
    ans = sol.isAnagram(s, t)

    print(ans)