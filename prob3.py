# Problem:

# Given a string, return a dictionary where the keys are characters and the values are the number of times each character appears.

# Ignore spaces.

# Example:
# Input: "hello world"
# Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}


string1 = "Hello World"

count_dict = {}


for char in string1.lower():
    if char == " ":
        continue
    if char in count_dict:
        count_dict[char] += 1
    else:
        count_dict[char] = 1
print(count_dict)