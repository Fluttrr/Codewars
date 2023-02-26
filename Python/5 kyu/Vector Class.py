"""
Vector class
https://www.codewars.com/kata/526dad7f8c0eb5c4640000a4
"""

import math

class Vector:
    def __init__(self, values):
        self.values = values
        
    def equals(self, other):
        if len(self.values) != len(other.values): return False
        i = 0
        for x, y in zip(self.values, other.values):
            if x != y: return False
        return True
    
    def __str__(self):
        res = "("
        for x in self.values:
            res += str(x) + ","
        res = res[:-1] + ")"
        return res
    
    def add(self, other):
        if len(self.values) != len(other.values): raise Exception
        result = list()
        for x, y in zip(self.values, other.values):
            result.append(x + y)
        return Vector(result)
            
        
    def subtract(self, other):
        if len(self.values) != len(other.values): raise Exception
        result = list()
        for x, y in zip(self.values, other.values):
            result.append(x - y)
        return Vector(result)
        
    def dot(self, other):
        if len(self.values) != len(other.values): raise Exception
        result = 0
        for x, y in zip(self.values, other.values):
            result += x * y
        return result
    
    def norm(self):
        result = 0
        for x in self.values:
            result += x ** 2
        return math.sqrt(result)
