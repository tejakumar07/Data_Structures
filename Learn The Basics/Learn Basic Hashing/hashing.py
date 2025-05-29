# This Program is not Hashing This will give the idea of why we require hashing
def function(length, num):
    # Initialize a counter for the occurrences of the target number
    count = 0

    # Loop through the entire list
    for i in range(length):
        if a[i] == num:  # If the current element matches the target
            count += 1  # Increment the count

    # After the loop, check if the target number was not found
    if count == 0:
        return "Not Found"  # If no occurrences, return "Not Found"
    
    # Return the total count of occurrences
    return count

# Explanation of why hashing is better:
# 1. **Inefficient Repeated Search**:
#    - If we frequently need to find the count of different target numbers,
#      this approach requires scanning the entire list every time. This is
#      inefficient as the complexity is O(n) for each query.

# 2. **Hashing Can Reduce Time Complexity**:
#    - Hashing allows us to store the frequency of each number in the list
#      in a dictionary (or hash map).
#    - This makes the lookup for any number O(1) on average instead of O(n),
#      reducing overall computational cost.

# 3. **Better for Large Datasets**:
#    - For a large list, this approach becomes slow due to repeated traversals.
#    - Hashing preprocesses the data once, and subsequent queries are faster.

if __name__ == "__main__":
    # Define the list of elements
    a = [1, 3, 1, 4, 5, 6, 7, 9, 7, 4, 7, 12, 54, 66, 86, 993, 22, 3, 7, 1, 2, 6, 3, 4, 7, 5, 9]
    length = len(a)  # Get the length of the list
    target = int(input("What's the target: "))  # Input the target number
    print(function(length, target))  # Call the function
