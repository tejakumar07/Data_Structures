# Optimal Solution

def LongestConsecutiveSequence(nums):
    
    if len(nums) == 0:
        return
    
    length = 0
    st = set()

    for num in nums:
        st.add(num)
    
    for it in st:
        if it-1 not in st:
            count = 1
            x = it + 1
            while x in st:
                x += 1
                count += 1
            length = max(length, count)
    return length

if __name__ == "__main__":
    arr = [100, 200, 1, 2, 3, 4]
    print(LongestConsecutiveSequence(arr))