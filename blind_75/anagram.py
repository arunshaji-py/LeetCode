from collections import Counter

class Solutions:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        #build a frequency map for s using a dictionary

        count = {}
        for char in s:
            count[char] = count.get(char,0) + 1 
        
        #substract using t
        for char in t:
            if char not in count:
                return False
            count[char] -= 1
            
            if count[char] < 0:
                return False
        return True



""" in python [] means 'go fetch/store something inside this counter' """