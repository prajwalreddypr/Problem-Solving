# Problem:

# Given a list of integers, return a new list containing only the numbers that appear more than once in the original list.

# But the order of appearance must be preserved.

# Example:
# Input: [1, 2, 2, 3, 1, 4, 2]
# Output: [1, 2, 2, 1, 2]

list = [1, 2, 2, 3, 1, 4, 2]

dict_count = {}
final_list = []

for item in list:
    if item in dict_count:
        dict_count[item] += 1
    else:
        dict_count[item] = 1
        

for item in list:
    if dict_count[item] > 1:
        final_list.append(item)

print(final_list)