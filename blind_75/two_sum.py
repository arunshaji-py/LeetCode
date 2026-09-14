#define the class using camel casing
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range (i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                
# Notes:

# for i in nums VS for in in range(nums) working:
# for in in nums iterates over the 'values' in nums 
# for in in range(nums) iterates over the 'indices' of list nums
# time complexity = O(n^2) because we use two for loops. For every element, you check every element after that.