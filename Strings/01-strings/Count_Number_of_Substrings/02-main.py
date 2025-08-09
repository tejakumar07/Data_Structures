def countSubstringsExactlyK(s, K):
    def atMostK(s, K):
        freq = {}
        left = 0
        total = 0
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            
            while len(freq) > K:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1
            
            total += right - left + 1
        return total
    
    return atMostK(s, K) - atMostK(s, K - 1)


# Example
s = "pqpqs"
k = 2
ans = countSubstringsExactlyK(s, k)
print(ans)  # 7
