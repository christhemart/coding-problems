'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that
contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct
characters is "bcb".
'''

def longest_distinct_substr(string, length):
   max_length = 0
   max_string = ''

   for index1 in range(len(string)):
       char_set = set()

       for index2 in range(index1, len(string)):
           if string[index2] not in char_set:
               if len(char_set) >= length:
                   index2 -= 1
                   break
               else:
                   char_set.add(string[index2])

       if (index2-index1) + 1 > max_length:
           max_length = (index2-index1) + 1
           max_string = string[index1:index2+1]

       if max_length >= len(string) - index1:
           break

   return max_length, max_string


print(longest_distinct_substr('abcba', 2))