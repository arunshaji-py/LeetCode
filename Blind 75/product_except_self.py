# problem number 238
class Solution:
    def productExpectSelf(self, nums: list[int])-> list[int]:
        n = len(nums)

        #initialise a list with n number of 1's
        prefix = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i-1]
        
        sufix = [1] * n

        for i in range(n -2, -1, -1):
            sufix[i] = sufix[i+1] * nums[i+1]
        
        #combine the two lists
        return[prefix[i] * sufix[i] for i in range(n)]
""" explanation and logic behind the code
make two lists, prefix and sufix
start from index 1 for the prefix.
nake products store it in prefix list 

And for the sufix start from n-2 , to -1 and shifting - 1


"""

        
            


