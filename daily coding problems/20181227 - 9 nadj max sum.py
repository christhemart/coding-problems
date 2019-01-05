'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of
non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
[5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
'''

def nadj_max_sum(arr):
    inclusive = 0
    exclusive = 0
    for i in arr:
        new_exclusive = max(exclusive, inclusive)
        inclusive = exclusive + i
        exclusive = new_exclusive
    return max(exclusive, inclusive)


assert nadj_max_sum([2, 4, 6, 2, 5]) == 13
assert nadj_max_sum([5, 1, 1, 5]) == 10
