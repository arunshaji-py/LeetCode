class Solution:
    def threeSum(self, nums: list[int])-> list[list[int]]:
        nums.sort() # by default python uses Timsort( which is a combination of Merge sort and insertion sort)
        result = []

        #define an outer loop to fix a number at a time as the 'anchor'.say for example, if we set -1 once,
        #then that number shouldn't be anchored again.

        for i in range(len(nums)-2):
            #skip the duplicate for the fixed number.
            if i>0 and nums[i] ==nums[i-1]:
                continue

            #early exit: smallest possible sum is already > 0, because after sorting the list should be having 0 or negetive numbers to get 0
            #on while doing total.
            if nums[i] > 0:
                break

            #declare the two pointers
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
            #check for sucess
            if total == 0:
                result.append([nums[i],nums[left],nums[right]])

            #if total is not zero, continue the operations

            #skip the duplicate value of left pointer
                while left < right and nums[left] == nums[left+1]:
                    left += 1
            #skip the duplicate value of the right pointer
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
            
            #after finding a successful triplet move the pointer inward.
                left += 1
                right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1
                
        return result



            



