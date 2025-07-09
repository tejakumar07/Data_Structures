# Optimal Solution - I

def merging_two_sorted_arrays_without_extra_space(nums1, nums2):
  n = len(nums1)
  m = len(nums2)
  left = n - 1
  right = 0

  while left >= 0 and right < m:
    if nums1[left] > nums2[right]:
      nums1[left], nums2[right] = nums2[right], nums1[left]
      left -= 1
      right += 1
    else:
      break
  nums1.sort()
  nums2.sort()
if __name__ == "__main__":
  arr1 = [1, 3, 5, 7, 9]
  arr2 = [2, 4, 6, 8, 10, 12, 14, 16, 15, 18]
  print("Before Merging: ")
  print(arr1, arr2)
  merging_two_sorted_arrays_without_extra_space(arr1, arr2)
  print("After Merging: ")
  print(arr1, arr2) 