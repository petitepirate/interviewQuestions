# This problem was asked by Two Sigma.

# Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform 
# probability, implement a function rand5() that returns an integer from 1 to 5 (inclusive).

# _______________________________________________________________________________________
# Solution
# This problem is simpler than going from rand5() to rand7(). We'll do something similar:

# Roll rand7().
# If the result is between 1 and 5, then return it.
# If the result is 6 or 7, then reroll.
# Since the distribution of [1, 5] is uniform -- each has a 1/7 chance of being rolled, 
# then our rand5() will be uniform.

def rand5():
    r = rand7()
    if 1 <= r <= 5:
        return r
    return rand5()

# This could potentially take forever (although with a very low probability), if we keep 
# on getting 6 or 7s.
