import math
# Calculate the count of digits in 'n'
# using logarithmic operation log10(n) + 1.

n = int(input("What's the Number: "))

digit = int(math.log10(n)+1)
    # The expression int(math.log10(n) + 1)
    # calculates the number of digits in 'n'
    # and casts it to an integer.
    
    # Adding 1 to the result accounts
    # for the case when 'n' is a power of 10,
    # ensuring that the count is correct.
   
    # Finally, the result is cast
    # to an integer to ensure it is rounded
    # down to the nearest whole number.

print(digit)