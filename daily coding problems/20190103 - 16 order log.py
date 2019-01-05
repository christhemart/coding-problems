'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log.
Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be
smaller than or equal to N.

You should be as efficient with time and space as possible.
'''

class Order:
   def __init__(self, order_id):
       self.order_id = order_id

   def get_order_id(self):
       return self.order_id


class OrderLog():
   def __init__(self):
       self.log = []

   def record(self, order):
       self.log.append(order)

   def get_last(self, i):
       return self.log[-i].get_order_id()


log = OrderLog()

for order_id in range(26):
   log.record(Order(order_id))

print(log.get_last(1))
print(log.get_last(5))
print(log.get_last(21))