'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a stream of elements too large to store in memory, pick a random element
from the stream with uniform probability.
'''

import random


# test class to include storing indexes to later average
# real class does not need to store indexes
class StreamSampling:
   def __init__(self, sample_size):
       self.sample_size = sample_size
       self.samples = []
       self.indexes = []
       self.sample_iteration = 0

   def sample(self, element, index):
       self.sample_iteration += 1
       if self.sample_iteration <= self.sample_size:
           self.samples.append(element)
           self.indexes.append(index)
       elif random.randint(1, self.sample_iteration) <= self.sample_size:
           i = random.randint(0, self.sample_size-1)
           self.samples[i] = element
           self.indexes[i] = index


# Randomly generate 10,000 real numbers between 0 and 1.
# Sample 1,000 elements 1 element at a time like a stream.
# If the sample has uniform probability then the average of the indexes
# should be around 5,000.
# Do this 5 times.
for _ in range(5):
   ss = StreamSampling(1000)

   for index, element in enumerate([random.random() for _ in range(10000)]):
       ss.sample(element, index)

   print(sum(ss.indexes) / ss.sample_size)


# To get just 1 element with uniform probability with an unknown size stream
# we could then just instantiate the class with sample size 1 and feed in
# streaming data and be able to get a uniform probability sampling.

# actual class
class StreamSampling:
   def __init__(self, sample_size):
       self.sample_size = sample_size
       self.samples = []
       self.sample_iteration = 0

   def sample(self, element):
       self.sample_iteration += 1
       if self.sample_iteration <= self.sample_size:
           self.samples.append(element)
       elif random.randint(1, self.sample_iteration) <= self.sample_size:
           i = random.randint(0, self.sample_size-1)
           self.samples[i] = element


ss = StreamSampling(1)
some_stream = []

for element in some_stream:
   ss.sample(element)