class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #use a dictionary to keep track of the elements.
        last_seen = {}
        left = 0 
        max_length = 0

        #use enumerate to store the index and its value in the dictionary

        for right, char in enumerate(s):
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1
            
            last_seen[char] = right
            max_length = max (max_length, right - left + 1)
        
        return max_length


    




""" 
Notes
- This problem is the classic sliding window problem.
- The idea is to store the element in a data structure that enables quick check for the element later on.
- The best solution is using python dictionary for this problem.
- In dictionary there is not concept of index. It's always key- value pair.
- In the problem the char in the string s will be stored as follows - { a: 0 , b: 1, c:2 }
"""

