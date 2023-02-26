"""
Simplifying multilinear polynomials
https://www.codewars.com/kata/55f89832ac9a66518f000118

This solution is very ugly and long but it works so whatever lol
"""

import re

def simplify(poly):
    
    if poly[0] == "+": poly = poly[1:]
    
    # Divide string into positive parts and negative parts
    elementsPos = re.findall("(?<=\+).*?(?=\+|-|$)", poly)
    if poly[0] != "-": elementsPos.append(re.search("^.+?(?=\+|-)", poly).group())
    elementsNeg = re.findall("(?<=-).*?(?=\+|-|$)", poly)
    
    # Split each element into its letters and its value
    elementsPos = [ [x[1:], int(x[0])] if x[0].isnumeric() else [x, 1] for x in elementsPos ]
    elementsNeg = [ [x[1:], int(x[0])] if x[0].isnumeric() else [x, 1] for x in elementsNeg ]
    
    # Sort each string alphabetically
    elementsPos = [["".join(sorted(x[0])), x[1]] for x in elementsPos]
    elementsNeg = [["".join(sorted(x[0])), x[1]] for x in elementsNeg]
    
    # Combine duplicate elements
    for x in elementsNeg:
        for y in elementsNeg[elementsNeg.index(x)+1:]:
            if x[0] == y[0]: 
                y[1] += x[1]
                elementsNeg.remove(x)      
    
    for x in elementsPos:
        for y in elementsPos[elementsPos.index(x)+1:]:
            if x[0] == y[0]: 
                y[1] += x[1]
                elementsPos.remove(x)
           
    # Subtract negative elements from exisiting positive ones
    for x in elementsPos:
        for y in elementsNeg:
            if x[0] == y[0]: x[1] -= y[1]
                
    # Add other negative elements
    for x in elementsNeg:
        found = False
        for y in elementsPos:
            if x[0] == y[0]: found = True
        if not found:
            elementsPos.append([x[0], -x[1]])
            
    # Sort all elements alphabetically
    elementsPos = sorted(elementsPos, key=lambda x : elementsPos[elementsPos.index(x)][0])
            
    # Determine max string length
    longestSeq = 0
    for x in elementsPos:
        if len(x[0]) > longestSeq: longestSeq = len(x[0])
     
    # Convert elements into string
    result = ""
    i = 1
    while i <= longestSeq:
        for x in elementsPos:
            if len(x[0]) == i and x[1] != 0:
                result += "+" if x[1] > 0 else "-"
                if abs(x[1]) != 1: result += str(abs(x[1]))
                result += x[0]
        i += 1
        
    if result[0] == "+": result = result[1:]
            
    return(result)
