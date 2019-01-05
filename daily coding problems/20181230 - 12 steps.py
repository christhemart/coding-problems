'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps
at a time. Given N, write a function that returns the number of unique ways you
can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb
any number from a set of positive integers X? For example, if X = {1, 3, 5}, you
could climb 1, 3, or 5 steps at a time.
'''

def stairs(steps_left, step_sizes):
   cache = [0 for _ in range(steps_left+1)]
   cache[0] = 1
   for index in range(steps_left + 1):
       cache[index] += sum(cache[index-step] for step in step_sizes if index-step > 0)
       if index in step_sizes:
           cache[index] += 1
   return cache[-1]


assert stairs(4, [1, 2]) == 5

print(stairs(10, [1, 3, 5]))