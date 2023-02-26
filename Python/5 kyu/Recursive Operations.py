"""
Calculating with Functions
https://www.codewars.com/users/Flutter/completed_solutions

This looks very ugly and dumb and long but the length is actually necessary and if you read the task its kinda dumb itself
"""

def zero(a=0):
    if type(a) == dict: return eval(a, 0)
    return 0
def one(a=0): 
    if type(a) == dict: return eval(a, 1)
    return 1
def two(a=0): 
    if type(a) == dict: return eval(a, 2)
    return 2
def three(a=0): 
    if type(a) == dict: return eval(a, 3)
    return 3
def four(a=0): 
    if type(a) == dict: return eval(a, 4)
    return 4
def five(a=0): 
    if type(a) == dict: return eval(a, 5)
    return 5
def six(a=0): 
    if type(a) == dict: return eval(a, 6)
    return 6
def seven(a=0): 
    if type(a) == dict: return eval(a, 7)
    return 7
def eight(a=0): 
    if type(a) == dict: return eval(a, 8)
    return 8
def nine(a=0): 
    if type(a) == dict: return eval(a, 9)
    return 9

def eval(a, n):
    if a.keys() == {"plus"}: return n + a.get("plus")
    if a.keys() == {"minus"}: return n - a.get("minus")
    if a.keys() == {"times"}: return n * a.get("times")
    if a.keys() == {"div"}: return n // a.get("div")

def plus(a): return {"plus":a}
def minus(a): return {"minus":a}
def times(a): return {"times":a}
def divided_by(a): return {"div":a}
