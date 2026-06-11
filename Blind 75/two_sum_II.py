class Solution:
    def twoSum(self,numbers: list[int], target: int)->list[int]:
        #define two pointers (which are basically the indices) to run from left and right
        left = 0
        right = len(numbers) - 1
        

        #define a while loop to iterate over the elements in numbers and check for target
        while left < right:
                total = numbers[left] + numbers[right]
                if total == target:
                     return [left+1 ,right+1]
                if total > target:
                     right -= 1
                if total < target:
                     left += 1
                     
                


"""

Notes

- Pointers hold the list index with them. use nums[left] and nums[right] to access the values on that index.
- In problems which asks if k numbers adds to a target. The trick is to 
  
"""