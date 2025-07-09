# Brute Force Approach

from typing import List

def merge_two_sorted_arrays(nums1: List[int], nums2: List[int]):
  n = len(nums1)
  m = len(nums2)
  nums3 = []
  left, right = 0, 0
  while left < n and right < m:
    if nums1[left] <= nums2[right]:
      nums3.append(nums1[left])
      left += 1
    elif nums1[left] > nums2[right]:
      nums3.append(nums2[right])
      right += 1
    else:
      nums3.append(nums1[left])
      left += 1
  while left < n:
    nums3.append(nums1[left])
    left += 1
  while right < m:
    nums3.append(nums2[right])
    right += 1
  for i in range(n + m):
    if i < n:
      nums1[i] = nums3[i]
    else:
      nums2[i-n] = nums3[i]
if __name__ == "__main__":
  arr1 = [1, 3, 5, 7, 9]
  arr2 = [2, 4, 6, 8, 10, 11, 12, 13, 14, 15]
  print("Before Merging: ->")
  print(arr1)
  print(arr2)
  merge_two_sorted_arrays(arr1, arr2)
  print("After Merging: ->")
  print(arr1)
  print(arr2)