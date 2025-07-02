def three_sum(nums):
    n = len(nums)
    st = set()

    if n == 0 or n == 1 or n == 2 or n == 3:
        return nums
    
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    temp = [nums[i], nums[j], nums[k]]
                    temp.sort()
                    st.add(tuple(temp))
    
    ans = [list(item) for item in st]
    return ans

if __name__ == "__main__":
    arr = [-1, 0, 1, 2, -1, -4]
    print(three_sum(arr))