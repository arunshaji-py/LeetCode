class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()

        for i in nums:
            if i in seen:
                return False
            else:
                seen.add(i)
        return True