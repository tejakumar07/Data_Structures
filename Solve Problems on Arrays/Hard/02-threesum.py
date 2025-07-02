def three_sum(nums):
    st = set()
    n = len(nums)
    
    for i in range(n):
        hashset = set()
        for j in range(i + 1, n):
            third = nums[i] + nums[j]
            if third in hashset:
                temp = [nums[i], nums[j], third]
                temp.sort()
                st.add(tuple(temp))
            hashset.add(nums[j])
    ans = [list(item) for item in st]
    return ans
if __name__ == "__main__":
    arr = [-1, 0, 1, 2, -1, -4]
    print(three_sum(arr))