class Solution:
    def validAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # now build a Hash map using dictionary to count the occurance of unique characters
        count = {}
        for char in s:
            #using the get function count the number of each characters.
            count[char] = count.get(char, 0)+ 1
        #now using another for loop iterate over each character in string t
        for char in t:
            if char not in count:
                return False
            else:
                count[char] -= 1
            if count[char] < 0:
                return False
        
        #if all the cases are valid
        return True


