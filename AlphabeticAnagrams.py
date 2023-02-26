"""
This approach splits the entirety of all possible permutations at 
each step (leftmost letter to rightmost letter) into the areas each 
possible letter would take up. For example: With BAC, we'd start at 
B and know that we have to be at least 1/3 into the number of all 
possible permutations. We add 1/3 of all possible permutations to the 
result and repeat for all letters, until we found the exact spot. 
What took me longest was figuring out how to incorporate repeated 
letters, but it's actually quite simple: They take up more space. 
For example, if you have the word BOOK, B is at 0, but K isn't at 
1/3, it's actually "earlier" because O takes up more space. In reality,
B starts at 0/4, K starts at 1/4 and O starts at 2/4.
"""

import math

def listPosition(word):
    if len(word) == 1: return 1
    
    result = 0
    for x in word:
        # Add corresponding left border
        result += sorted(list(word)).index(x) * calcPossibilities(word) // len(word) 
        word = word[1:]
        
    return(result + 1)

# Calculates the number of all possible permutations
def calcPossibilities(word):
    countsAbove1 = list()
    [countsAbove1.append(word.count(x)) for x in set(word) if word.count(x) > 1]
    return math.factorial(len(word)) // math.prod(math.factorial(x) for x in countsAbove1)
