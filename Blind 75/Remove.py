#define a Class (as coding convention, always use PascalCase for class names)
class Solution:
    #use snake case for function name
    def remove_duplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k += 1
        return k
    


