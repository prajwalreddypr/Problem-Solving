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





# #REVERSE A STRING

# str = "Paris is great"

# def reverse_string(str):
    
#     return str[::-1]

# print(reverse_string(str))


#HELLO WORLD
# print("Hello World")


# name = input("Enter your name: ")
# print(name)

# num1 = int(input("Number 1: "))
# num2 = int(input("Number 2: "))
# print("sum", num1 + num2)


# str = input("Enter a string: ")
# print(len(str))


#GIVEN A STRING, PRINT FIRST AND LAST CHAR
# str = "Prajwal"
# print(f"First char: {str[0]}")
# print(f"Last char: {str[-1]}")


# #REVERSE A STRING
# str = "this is long string"
# print(str[::-1])


# str = "Paris is lovely"
# print(str.upper())
# print(str.lower())


# #appending an item to a list
# arr = [10,20, 30]
# arr.append(40)
# # print(arr)
# arr.remove(20)
# print(arr)


#SUMMING A LIST OF NUMBERS
# nums = [1,2,3,4,5]
# print(sum(nums))
# sum = 0

# for num in nums:
#     sum += num

# print(sum)




# #MAX NUMBER INA LIST
# nums = [1,2,3,4,5,6]
# # print(max(nums))

# max_num = nums[0]
# for num in nums:
#     if num > max_num:
#         max_num = num
# print(max_num)



#CHECKING IF AN ELEMENT EXISTS IN A LIST
# arr = [10,43,4,34,34,5,4,67,78]
# print(60 in arr)
# print(67 in arr)


#COUNTING OCCUREENCES OF an element
# arr = [1,2,3,4,3,4,5,6,6,7]
# # print(arr.count(3))

# count = {}

# for item in arr:
#     if item in count:
#         count[item] += 1
#     else:
#         count[item] = 1

# print(count)




#LOOP THROUGH A StriNG AND COUNT VOWELS
