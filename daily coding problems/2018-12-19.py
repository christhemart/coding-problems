'''
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the
list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

def sum_exists(list, target_sum):
    for index1 in range(len(list)):
        for index2 in range(index1+1,len(list)):
            if list[index1] + list[index2] == target_sum:
                return True
    return False
