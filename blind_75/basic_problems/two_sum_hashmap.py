
#____Notes________
# 
# A dictionary in python is a Hash map. Under the hood python uses Hash map to store the key value pair.
# Hash map uses the 'key' to store the address of the memory address where the 'value' is has been stored.
# So this make the time complexity of searching a value O(1).
# Set() is a Hash map, but only with 'keys' no values.
class Solution:
    def two_sum(self,nums: list[int], target: int) -> list[int]:
        
        lookup = {}

        for index, num in enumerate(nums):
            complement = target - num
            if complement in lookup:
                return[lookup[complement],index]
            lookup[num] = index
            
        
