# import the special Counter 'dictionary' from the Collections library. Counter can count and keep the occurance of each element.
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        #step one, what we need
        need = Counter(t)  #stores { A: 1, B: 2 C: 3}etc
        window = {}        #Current window count

        #step 3 track the variables

        have = 0            #tracking how many characters satisfies the need
        required = len(need)    #tracks how unique char we need

        left = 0
        best_start = 0
        best_len = float("inf")

        #step 3 expand the right pointer

        for right in range(len(s)):
            char = s[right] #char holds the character at the index 'right'

            #now, add this character to the window
            window[char] = window.get(char,0) + 1

            #check if this char satisfies the requirement
            if char in need and window[char] == need[char]:
                have += 1
            
            #step 4: now shrink from left until window is valid.

            while have == required:
                #update best len
                if(right - left + 1) < best_len:
                    best_len = right - left + 1
                    best_start = left
            

            #remove the character from the left
            left_char = s[left]
            window[left_char] -= 1

            #check if removing it breaks the requirement
            if left_char in need and window[left_char]< need[left_char]:
                have -= 1

            left += 1
        return s[best_start: best_start+ best_len] if best_len != float ("inf") else ""
    
    






