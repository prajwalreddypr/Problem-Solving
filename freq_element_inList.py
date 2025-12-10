#MOST FREQUENT ELEMENT IN THE LIST(FIRST OCCURENCE ONLY)


def freq_elem(lst):
    max_count = 0
    most_freq = None
    count = {}
    
    for item in lst:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
            
    for key, value in count.items():
        if value > max_count:
            max_count = value
            most_freq = key
            
    return most_freq

print(freq_elem([1,1,2,3,4,4,5]))