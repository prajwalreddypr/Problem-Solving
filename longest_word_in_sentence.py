#RETURNING THE LONGEST WORD IN THE SENTENCE

def longest_word(str):
    words = str.split()
    longest = words[0]
    
    for word in words:
        if len(word) > len(longest):
            longest = word
            
    return longest    
        
    
print(longest_word("Heyy bonjour paris"))