# This problem was asked by Google.

# Determine whether a doubly linked list is a palindrome. What if it’s singly linked?

# For example, 1 -> 4 -> 3 -> 4 -> 1 returns True while 1 -> 4 returns False.

#_______________________________________________________________________________________
# Solution
# This problem can be solved for both singly and doubly linked list by using iterators.

# We can then create an iterator over the first node, and another iterator over the reverse 
# of the linked list. Then compare that the two are the same.

# This would take O(N) space and time.

def get_values(node):
    while node:
        yield node.val
        node = node.next


def is_palindrome(node):
    values = get_values(node)
    values_reversed = reversed(list(get_values(node))) # O(N) space

    return all(x == y for x, y in zip(values, values_reversed))
