# Brute Force Approach
# Linear Search from the maximum book size to the total sum of all books

# Helper function to count how many students are needed
# if we allocate books such that no student gets more than `pages`
def countStudents(arr, pages):
    n = len(arr)
    students = 1   # At least one student is needed
    pagesStudent = 0  # Pages assigned to current student

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
# any student has to read (brute-force)
def findPages(arr, n, m):
    # If number of students is more than number of books, allocation not possible
    if m > n:
        return -1

    low = max(arr)  # Lower bound of answer (minimum max pages a student must read)
    high = sum(arr) # Upper bound (if one student reads all the books)

    # Try every value from low to high to find the minimum valid answer
    for i in range(low, high + 1):
        # If for this `i` pages, we can divide books among `m` students
        if countStudents(arr, i) == m:
            return i  # First valid solution is the minimum because we're going from low to high

    return low  # Fallback (this won't actually be reached in this problem)

# Driver Code
if __name__ == "__main__":
    arr = [12, 34, 67, 90]  # Book pages
    n = 4                   # Number of books
    m = 2                   # Number of students
    ans = findPages(arr, n, m)
    print("The answer is:", ans)
