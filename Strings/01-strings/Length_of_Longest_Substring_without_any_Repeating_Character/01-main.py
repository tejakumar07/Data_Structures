# Brute Force Approach

def lengthOfLongestSubstring(s):
    n = len(s)
    
    if n == 0:
        return 0
    
    maxi = 1
    
    for i in range(n):
        st = {}
        for j in range(i, n):
            if s[j] in st:
                maxi = max(maxi, j - i)
                break
            st[s[j]] = 1
        else:
            maxi = max(maxi, n - i)
    
    return maxi

if __name__ == "__main__":
    s = "abcabcbb"
    print(lengthOfLongestSubstring(s))    