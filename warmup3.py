#FIRST NON REPEATING CHARACTER INNA STRING

# def first_non_repeat(str):
#     count = {}
    
#     for char in str:
#         if char in count:
#             count[char] += 1
#         else:
#             count[char] = 1
    
#     for char in str:
#         if count[char] == 1:
#             return char
    
#     return None

# print(first_non_repeat("aaaabccccd"))




# #ROTATING A LIST BY K POSITIONS
# def rotate(lst, pos):
#     pos = pos % len(lst)
#     return lst[-pos: ] + lst[:-pos]


# print(rotate([1,2,3,4,5], 3))



#MOVING ALL ZEROS TO THE END OF THE LIST

# def move_zeros(lst):
#     j = 0;
    
#     for item in lst:
#         if item != 0:
#             lst[j] = item
#             j += 1
#     while j < len(lst):
#         lst[j] = 0
#         j += 1
        
#     return lst

# print(move_zeros([0,1,2,0,3,4,0,8]))






