from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int)-> list[int]:
        count = {}
        
        for num in nums:
            count[num] = count.get(num,0) + 1

            sorted_items = sorted(count.items(), key=lambda item: item[1], reverse =True)

        result =[]
        for item in sorted_items[:k]:
            result.append(item[0])
        return result
      
        
       
