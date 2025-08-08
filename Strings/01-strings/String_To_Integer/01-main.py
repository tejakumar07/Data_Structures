class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        sign = 1
        result = []
        is_seen = False

        for i in range(len(s)):
            
            if s[i] == "-" and is_seen == False:
                sign = -1
                is_seen = True
            
            elif s[i] == "+" and is_seen == False:
                sign = 1
                is_seen = True
            
            elif s[i].isdigit():
                result.append(s[i])
                is_seen = True
            
            else:
                break
        if not result:
            return 0

        ans = "".join(result)
        ans = int(ans)
        ans *= sign

        mini = -2 ** 31
        maxi = 2 ** 31 - 1

        if ans < mini:
            return mini
        if ans > maxi:
            return maxi
        
        return ans

if __name__ == "__main__":
    teja = Solution()
    s = "1337c0d3"
    print(teja.myAtoi(s))