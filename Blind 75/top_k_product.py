from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int)-> list[int]:
        count = Counter(nums)
        
        return [element for element,frequency in count.most_common(k)]

