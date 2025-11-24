# Given a list of integers, return a new list containing only the even numbers from the original list.

# Eg:
# Input: [1, 2, 3, 4, 5, 6]
# Output: [2, 4, 6]

list1 = [1,2,3,4,5,6,7,8,9,10]
new_list = []

for num in list1:
    if num % 2 == 0:
        new_list.append(num)

print(new_list)
        
