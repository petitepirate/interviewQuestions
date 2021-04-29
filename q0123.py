# This problem was asked by LinkedIn.

# Given a string, return whether it represents a number. Here are the different kinds of numbers:

# "10", a positive integer
# "-10", a negative integer
# "10.1", a positive real number
# "-10.1", a negative real number
# "1e5", a number in scientific notation
# And here are examples of non-numbers:

# "a"
# "x 1"
# "a -2"
# "-"

# _____________________________________________________________________________________________________
# Solution
# We can solve this problem bottom-up, starting from positive integers:

# A positive integer contains only digits.
# A negative integer starts with '-' and the rest is a positive integer.
# A positive decimal contains one '.' and the substrings before and after '.' are positive integers.
# A negative decimal starts with '-' and the rest is a positive decimal.
# A positive number is either a positive integer or decimal.
# A negative number is either a negative integer or decimal.
# A scientific notation number contains one 'e' and the substrings before and after 'e' are each either a 
# positive or negative number.
# And finally, a number is either a positive number, a negative number, or a scientific number.

def is_number(s):
    return is_positive_number(s) or is_negative_number(s) or is_scientific_number(s)


def is_scientific_number(s):
    if s.count('e') != 1:
        return False

    before_e, after_e = s.split('e')

    return ((is_positive_number(before_e) or is_negative_number(before_e))
        and (is_positive_number(after_e) or is_negative_number(after_e)))

def is_positive_number(s):
    return is_positive_integer(s) or is_positive_real(s)

def is_negative_number(s):
    return is_negative_integer(s) or is_negative_real(s)


def is_negative_real(s):
    return s.startswith('-') and is_positive_real(s[1:])

def is_positive_real(s):
    if s.count('.') != 1:
        return False

    integer_part, decimal_part = s.split('.')

    return is_positive_integer(integer_part) and is_positive_integer(decimal_part)

def is_negative_integer(s):
    return s.startswith('-') and is_positive_integer(s[1:])

def is_positive_integer(s):
    return s.isdigit()
