# Problem 6

# Task:

# Given a list of strings, return a dictionary where:

# Keys = first letter of each word (lowercase)

# Values = list of words starting with that letter (case-insensitive)

# Preserve the order of words as in the original list

# Example:

# Input: ["Apple", "banana", "apricot", "Blueberry", "cherry"]
# Output: {'a': ['Apple', 'apricot'], 'b': ['banana', 'Blueberry'], 'c': ['cherry']



fruits = ["Apple", "banana", "apricot", "Blueberry", "cherry"]


count_dict = {}

for fruit in fruits:
    if fruit == " ": #edge case taken care off early
        continue
    
    key = fruit[0].lower() #converting first index of each item,  to lower
    
    #print(key) -> this prints the keys a,b,a,b,c
    
    if key in count_dict:
        count_dict[key].append(fruit)
    else:
        count_dict[key] = [fruit] #[fruit] and not fruit because, we need to append to that list if more items are there. Hencce [fruit]. we are appending a list.
        
print(count_dict)


