def count_k_distinct(s, k):
    n = len(s)
    cnt = 0
    
    for i in range(n):
        current = ""
        st = set()
        
        for j in range(i, n):
            ch = s[j]
            current += ch
            st.add(ch)
            
            if len(st) == k:
                cnt += 1
            elif len(st) > k:
                break
    return cnt
if __name__ == "__main__":
    s = "abcabc"
    k = 2
    print(count_k_distinct(s, k))
