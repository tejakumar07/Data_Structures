class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        keys = list(s)
        for c in t:
            if c not in keys:
                return False
            keys.remove(c)
        return True

if __name__ == "__main__":
    sol = Solution()
    
    s = "anagram"
    t = "nagaram"
    ans = sol.isAnagram(s, t)
    
    print(ans)