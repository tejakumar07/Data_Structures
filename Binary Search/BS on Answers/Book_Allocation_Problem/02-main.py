# Optimal Approach
# Using Binary Search to minimize the maximum pages allocated to a student

# Helper function to count how many students are needed
# if we allocate books such that no student gets more than `pages`
def countStudents(arr, pages):
    n = len(arr)
    students = 1           # At least one student is needed
    pagesStudent = 0       # Pages assigned to current student

    for i in range(n):
        # If adding this book doesn't exceed the max pages allowed
        if pagesStudent + arr[i] <= pages:
            pagesStudent += arr[i]  # Allocate book to current student
        else:
            # Otherwise, assign the book to next student
            students += 1
            pagesStudent = arr[i]  # Start counting pages for new student

    return students  # Total number of students needed for given `pages` limit

# Main function to find the minimum number of maximum pages
# any student has to read (using binary search)
def findPages(arr, n, m):
    # If number of students is more than number of books, allocation not possible
    if m > n:
        return -1

    low = max(arr)         # Lower bound of answer: at least one book with max pages
    high = sum(arr)        # Upper bound: one student takes all books
    result = -1            # To store the minimum possible max pages

    while low <= high:
        mid = (low + high) // 2      # Mid value = current maximum pages per student allowed
        requiredStudents = countStudents(arr, mid)

        if requiredStudents > m:
            # Too many students needed → Increase the allowed pages
            low = mid + 1
        else:
            # Try to minimize further → This `mid` might be our answer
            result = mid
            high = mid - 1

    return result  # Minimum of the maximum pages that can be allocated

# Driver Code
if __name__ == "__main__":
    arr = [12, 34, 67, 90]  # Book pages
    n = 4                   # Number of books
    m = 2                   # Number of students
    ans = findPages(arr, n, m)
    print("The answer is:", ans)
