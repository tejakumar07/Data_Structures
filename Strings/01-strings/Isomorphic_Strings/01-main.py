class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mppST, mppTS = {},  {}
        
        for c1, c2 in zip(s, t):
            
            if (c1 in mppST and mppST[c1] != c2) or (c2 in mppTS and mppTS[c2] != c1):
                return False
            
            mppST[c1] = c2
            mppTS[c2] = c1
        
        return True

if __name__ == "__main__":
    teja = Solution()
    print(teja.isIsomorphic(s ="egg", t = "add"))
    print(teja.isIsomorphic(s = "foo", t = "bar"))