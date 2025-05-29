def function(i, n):
    # This is the Base Condition
    if i > n:
        return
    print("Sneha")
    function(i + 1, n)

if __name__ == "__main__":
    n = int(input("N: "))
    function(1, n)