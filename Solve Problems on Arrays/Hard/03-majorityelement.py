
def majorityElement(nums):
    element1 = None
    element2 = None
    cnt1 = 0
    cnt2 = 0

    for num in nums:
        if element1 == num:
            cnt1 += 1
        elif element2 == num:
            cnt2 += 1
        elif cnt1 == 0:
            element1 = num
            cnt1 = 1
        elif cnt2 == 0:
            element2 = num
            cnt2 = 1
        else:
            cnt1 -= 1
            cnt2 -= 1

    cnt1 = cnt2 = 0
    for num in nums:
        if num == element1:
            cnt1 += 1
        elif num == element2:
            cnt2 += 1

    final = []
    n = len(nums) // 3
    if cnt1 > n:
        final.append(element1)
    if cnt2 > n:
        final.append(element2)

    return final

if __name__ == "__main__":
    nums = [3,2,3]
    print(majorityElement(nums))
