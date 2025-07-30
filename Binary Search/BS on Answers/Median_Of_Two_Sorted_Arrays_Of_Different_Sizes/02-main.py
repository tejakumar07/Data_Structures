def medianOfTwoSortedArrays(nums1, nums2):
    n1, n2 = len(nums1), len(nums2)
    n = n1 + n2
    cnt = 0
    indx2 = n // 2
    indx1 = indx2 - 1
    elem1 = elem2 = -1
    i = j = 0

    while i < n1 and j < n2:
        if nums1[i] <= nums2[j]:
            if cnt == indx1:
                elem1 = nums1[i]
            if cnt == indx2:
                elem2 = nums1[i]
            i += 1
        else:
            if cnt == indx1:
                elem1 = nums2[j]
            if cnt == indx2:
                elem2 = nums2[j]
            j += 1
        cnt += 1

    while i < n1:
        if cnt == indx1:
            elem1 = nums1[i]
        if cnt == indx2:
            elem2 = nums1[i]
        i += 1
        cnt += 1

    while j < n2:
        if cnt == indx1:
            elem1 = nums2[j]
        if cnt == indx2:
            elem2 = nums2[j]
        j += 1
        cnt += 1

    if n % 2 == 1:
        return elem2
    return (elem1 + elem2) / 2.0

# Example usage
if __name__ == "__main__":
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(medianOfTwoSortedArrays(nums1, nums2))
