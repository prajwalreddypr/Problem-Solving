# Problem:

# Given a list of integers, return a dictionary where

# keys = numbers

# values = how many times each number appears

# Example:
# Input: num_list = [1, 2, 2, 3, 1, 4, 2]
# Output: {1: 2, 2: 3, 3: 1, 4: 1}

num_list = [1, 2, 2, 3, 1, 4, 2]

dict_count = {}

for num in num_list:
    if num in dict_count:
        dict_count[num] += 1
    else:
        dict_count[num] = 1

print(dict_count)




