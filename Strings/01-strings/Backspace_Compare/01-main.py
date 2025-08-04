class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        new1 = []
        new2 = []

        for ch in s:
            if ch == "#":
                if len(new1) != 0:
                    new1.pop()
                    continue
                else:
                    continue
            new1.append(ch)
        
        for ch in t:
            if ch == "#":
                if len(new2) != 0:
                    new2.pop()
                    continue
                else:
                    continue
            new2.append(ch)
        
        return new1 == new2

if __name__ == "__main__":
    s = "ab#c"
    t = "ad#c"
    teja = Solution()
    print(teja.backspaceCompare(s, t))