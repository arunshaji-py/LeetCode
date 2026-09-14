class Solution:
    def maxSubarray(self,nums: list[int])-> list[int]:
        current_max = nums[0]
        current_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num,current_sum +num)
            current_max = max(current_sum, current_max)
        
        return current_max