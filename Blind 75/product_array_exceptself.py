# problem number 238
class Solution:
    def productExceptSelf(self, nums: list[int])-> list[int]:

        answer =[1]* len(nums)
        prefix = 1

        for i in range(len(nums)):
            answer[i] = prefix
            prefix = prefix * nums[i]
        
        suffix = 1
        for i in range(len(nums)-1,-1,-1):
            answer[i] *= suffix
            suffix = suffix * nums[i]
        
        return answer