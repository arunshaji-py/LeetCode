class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left =0
        count = {}
        max_freq =0
        max_count =0

        #make the frequency counter
        for right in range(len(s)):
            count[s[right]] = count.get(s[right],0)+1
            max_freq = max(max_freq, count[s[right]])
        

        #check the present frequency with the k
            while(right - left +1) - max_freq > k:
                count[s[left]] -=1
                left += 1
            
            max_count = max(max_count,right - left +1)
        return max_count