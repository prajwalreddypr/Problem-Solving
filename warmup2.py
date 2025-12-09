#LEVEL 21 to LEVEL 40
# (Strings, lists, loops and basic logic)

#CONCATENATE 2 STRINGS
# str1 = "Hello"
# str2 = "World"
# result = f"{str1} {str2}"
# print(result)


#REPEAT A STRING 3 TIMES
# text = "hui"
# print(text * 3)


#STRING STARTS WITH A SUBSTRING
# text = "Python is lovely"
# print(text.startswith("Py"))
# print(text.startswith("Yt"))
# print(text.endswith("ly"))
# print(text.endswith("fsd"))




#index of a character in a string
# str = "ParisIsGreat"
# print(str.index("I"))


#NO of words in a string
# str = "This is the season of Christmas"
# words = str.split()
# print(len(words))



#REVERSE A LIST
# list = [1,2,3,4,5]
# list.reverse()
# print(list)



#SORTING A LIST OF NUMBERS
# numbers = [2,43,5,4,5,3,2,5,56]
# print(numbers)
# numbers.sort()
# print(numbers)




#SORTING LIST OF STRINGS ALPHABETICALLY
# strs = ["Alice", "Charlie", "Bob"]
# strs.sort()
# print(strs)



#REVERSE A STRING USING A LOOP
# str = "Paris and Python"
# rev = ""

# for char in str:
#     rev = char + rev

# print(rev)




#REMOVE DUPLICATES FROM LIST
# list = [1,2,3,4,1,2,1,3,6]
# count = {}
# dup = []

# for item in list:
#     if item in count:
#         count[item] += 1
        
#         if count[item] == 2:
#             dup.append(item)
#     else:
#         count[item] = 1

# print(dup) '



#GETTING THE LAST n ELEMENTS

# lst = [1,2,23,3,4,456,356,3,345]
# print(lst[-4::2])



#CHECKING IF LSIT IS EMPTY
# lst = [34,56,87,32]

# if not lst:
#     print("EMpty")
    



#SWAPPING 2 VARIABLES

# a, b = 34,54
# a,b = b,a
# print(a,b)


#REMOVING WHITE SPACE
# text = "   heyy bonjou   "
# print(text.strip())



#COUNTING VOWELS IN A STRING
# str = "Paris is cold and dark in winters"
# vowels = "aeieouAEIOU"
# count = 0


# for char in str:
#     if char in vowels:
#         count += 1
        
# print(count)





#REPLACING A SUBSTRING WIHT A STRING
text = "I love Java"
changed_text = text.replace("Java", "Python")
print(changed_text)