class Solution:
    def rob(self, nums: list[int])-> int:
        if not nums:
            return 0

        #declare a dp list and intialise it with 0 
        dp = [0]* len(nums)
        #check the length of nums,if its 1 return the answer as 1st node
        if len(nums) == 1:
            return nums[0]
        
        #enter the 1st two elements into the list
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        #use a for loop 
        for i in range(2,len(nums)):
            dp[i] = max(nums[i]+dp[i-2],dp[i-1])
        
        return dp[-1]
    