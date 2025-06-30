# Brute Force
def majority_element(nums):
  final = []
  for i in range(len(nums)):
    if nums[i] not in final:
      count = 0
      for j in range(len(nums)):
        if nums[i] == nums[j]:
          count += 1
      if count > len(nums) // 3:
        final.append(nums[i])
      if len(final) == 2:
        return final
if __name__ == "__main__":
  nums = [1, 1, 1, 1, 3, 3, 2, 2, 2, 2]
  print(majority_element(nums))