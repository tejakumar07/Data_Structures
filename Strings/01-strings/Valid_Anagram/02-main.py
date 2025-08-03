class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        freq_s = {}
        
        for ch in s:
            freq_s[ch] = freq_s.get(ch, 0) + 1
        
        for ch in t:
            if freq_s.get(ch, 0) == 0:
                return False
            freq_s[ch] -= 1

        return True

if __name__ == "__main__":
    sol = Solution()

    s = "anagram"
    t = "nagaram"
    ans = sol.isAnagram(s, t)

    print(ans)