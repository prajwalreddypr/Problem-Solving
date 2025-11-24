# Problem:

# Given a list of strings, return a new list containing only the strings that have length ≥ 5.

# Example:

# Input: ["hi", "apple", "sun", "python", "dog"]
# Output: ["apple", "python"]

animals = ["lion", "dog", "cat", "snake", "elephant", "Giraffe"]

new_list = []

for animal in animals:
    if len(animal) >= 5:
        new_list.append(animal)

print(new_list)
