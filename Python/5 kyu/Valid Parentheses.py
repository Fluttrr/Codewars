"""
Valid Parentheses
https://www.codewars.com/kata/52774a314c2333f0a7000688
"""

def valid_parentheses(string):
    count = 0 # To check balance
    broken = False # To check order
    for x in string:
        if x == "(": count += 1 # Checks balance of opening and closing
        if x == ")": 
            if count < 1: broken = True # Check is a closing parantheses is there without a leading opening one
            count -= 1 # Checks balance of opening and closing
    return not(count) and not(broken)
