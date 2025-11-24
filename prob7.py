'''
Problem 7

Task:

Given a list of integers, return a list of tuples where each tuple contains:

The number

Its frequency in the list

Order of numbers should be the same as their first appearance in the list.

Example:

Input: [4, 5, 4, 6, 7, 5, 8, 4]
Output: [(4, 3), (5, 2), (6, 1), (7, 1), (8, 1)]

'''

nums = [4, 5, 4, 6, 7, 5, 8, 4]

count_dict = {}

for num in nums:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1
 
as_tuple = tuple(count_dict.items())       
print(as_tuple)