"""
Memoized Fibbonaci
https://www.codewars.com/kata/529adbf7533b761c560004e5

Not solved properly as the list isn't private but this is fast too so I left it at that
"""

found = {0: 0, 1: 1}

def fibonacci(n):
    if n in [0, 1]:
        return n
    return getValue(n - 1) + getValue(n - 2)

def getValue(n):
    if n in found.keys(): return found[n]
    else:
        value = getValue(n - 1) + getValue(n - 2)
        found[n] = value
        return value
