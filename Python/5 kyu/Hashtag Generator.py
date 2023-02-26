"""
The Hashtag Generator
https://www.codewars.com/kata/52449b062fb80683ec000024
"""

def generate_hashtag(s):
    words = s.lower().strip().split(" ")
    
    s = ""
    for x in words:
        s += x.capitalize()
    
    if len(s) > 140 or len(s) < 1: return False
    return "#" + s
