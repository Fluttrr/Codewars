"""
Sum Strings as Numbers
https://www.codewars.com/kata/5324945e2ece5e1f32000370
"""

def sum_strings(x, y):
    # Make sure x is the bigger number as we will be adding y onto x
    if len(y) > len(x):
        h = x
        x = y
        y = h
        
    # Add extra 0 for carryover
    x = "0" + x
    
    numsX = list(x)
    numsY = list(y)
    i = len(numsY) - 1
    j = len(numsX) - 1
    
    # Simply add each decimal place, don't care about carrovers
    while i >= 0:
        numsX[j] = str(int(numsX[j]) + int(numsY[i]))
        i -= 1
        j -= 1
        
    # Distribute carryovers
    j = len(numsX) - 1
    while j >= 0:
        if int(numsX[j]) > 9:
            numsX[j-1] = str(int(numsX[j-1]) + int(numsX[j]) // 10)
            numsX[j] = str(int(numsX[j]) % 10)
        j -= 1
    
    
    s = "".join(numsX)
    
    # Remove leading 0s
    while len(s) > 0 and s[0] == "0":
        s = s[1:]
        
    return s if s != "" else "0"
