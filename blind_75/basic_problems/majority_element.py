class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count ={}

        majority_count = 0
        majority_element = None

        for num in nums:
            #define the frequency counter
            count[num] = count.get(num,0)+1

            if count[num] > majority_count:
                majority_count = count[num]
                majority_element = num
            
        return majority_element
    
        