# Better Solution

def majority_element(nums):
  elements = {}
  for num in nums:
    elements[num] = elements.get(num, 0) + 1
  n = len(nums) // 3
  
  final = []
  for key, value in elements.items():
    if value > n:
      final.append(key)
      if len(final) == 2:
        return final
  return final if len(final) > 0 else []
if __name__ == "__main__":
  nums = [1, 1, 1, 1, 3, 3, 2, 2, 2, 2]
  print(majority_element(nums))