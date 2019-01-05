'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a
Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
'''

from random import random


def estimate_pi(sample_size):
   total = 0
   for _ in range(sample_size):
       if random()**2 + random()**2 <= 1:
           total += 1
   return round(4 * (total / sample_size), 3)


for _ in range(5):
   print(estimate_pi(10000))