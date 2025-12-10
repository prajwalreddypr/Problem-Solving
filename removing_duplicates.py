#REMOVING THE CONSECUTIVE DUPLICATES
#EX aaabbc -> abc

def remove_cons_dup(str):
    
    result = [str[0]]
    
    for char in str[1: ]:
        if char != result[-1]:
            result.append(char)
            
    return "".join(result)

print(remove_cons_dup("aaabbbcaabbac"))