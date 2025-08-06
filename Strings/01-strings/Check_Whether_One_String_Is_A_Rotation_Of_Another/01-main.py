# Optimal Approach

class Solution:
    def rotateString(self, sneha: str, teja: str) -> bool:
        return len(sneha) == len(teja) and sneha in teja + teja

if __name__ == "__main__":
    s = "abcde"
    goal = "cdeab"
    teja = Solution()
    print(teja.rotateString(s, goal))