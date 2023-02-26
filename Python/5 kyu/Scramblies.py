"""
Scramblies
https://www.codewars.com/kata/55c04b4cc56a697bb0000048
"""

def scramble(s1, s2):
    s2chars = set(s2)
    for x in s2chars:
        if s1.count(x) < s2.count(x): return False
    return True
