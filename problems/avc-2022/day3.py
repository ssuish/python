def split_items(items):
    compartment1 = set()
    compartment2 = set()
    
    mid = len(items) // 2
    compartment1 = set(items[:mid])
    compartment2 = set(items[mid:])
        
    return compartment1, compartment2 

def Main():
    path = "D:\\dev\\ssuish-repo\\python\\problems\\avc-2022\\data\\day3.txt"
    
    # Priorities
    lowercase = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
        'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
        't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y':25, 'z': 26
                }
    uppercase = {
        'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36,
        'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45,
        'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52
    }
    
    # Test cases
    #file = [
    #    "vJrwpWtwJgWrhcsFMMfFFhFp",
    #    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    #    "PmmdzqPrVvPwwTWBwg",
    #    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    #    "ttgJtRGJQctTZtZT",
    #    "CrZsJsPPZsGzwwsLwLmpwMDw"
    #]
    
    priority_sum = 0
    shared_items = []
    
    # Case 1
    # with open(path, 'r') as file:
    #   for line in file:
    #        chars = line.strip()
    #        compartmentL, compartmentR = split_items(chars)
    #        items = compartmentL & compartmentR
    #        shared_items.append(*items) # unpacking the set   
    # for i in shared_items:
    #    if i in lowercase:
    #        priority_sum += lowercase[i]
    #    elif i in uppercase:
    #        priority_sum += uppercase[i]
            
    # Case 2
    rucksacks = []
    group = []
    
    with open (path, 'r') as file:
        for line in file:
            # Group every 3 lines into one set
            line = line.strip()
            group.append(set(line))
        
    i = 0
    while i < len(group):
        rucksacks.append(group[i] & group[i+1] & group[i+2]) # intersection of 3 sets
        i += 3
        
    for rucksack in rucksacks:
        for item in rucksack:
            if item in lowercase:
                priority_sum += lowercase[item]
            elif item in uppercase:
                priority_sum += uppercase[item]
        
    print("Priority sum: ", priority_sum)
        

if __name__ == '__main__':
    Main()