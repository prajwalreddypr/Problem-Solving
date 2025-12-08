# def greet(name):
#     print(f"Heyy this is {name}. today is a rainy day")
    
# greet("Prajwal")


# def even_odd(num):
#     if num % 2 == 0:
#         return "even"
#     elif num == 0:
#         return "zero"
#     else:
#         return "odd"
    
# print(even_odd(56));


# def sum_of_n(num):
#     sum = 0
#     for i in range(1, num+1):
#         sum += i
#     return sum

# print(sum_of_n(6))

# def count_greater_than_10(arr):
#     count = []
#     for item in arr:
#         if item > 10:
#             count.append(item)
    
#     return count

# print(count_greater_than_10([1,2,3,4,46,345,543,56]))




#first index of the occurence of the element

# arr = [1,2,6,4,5,6,3,2]

# def first_occur(arr):
#     index = 0
#     for item in arr:
#         if arr[index] == 6:
#             return index
#         index += 1

# print(first_occur(arr))





#REVERSE A STRING

str = "Paris is great"

def reverse_string(str):
    
    return str[::-1]

print(reverse_string(str))