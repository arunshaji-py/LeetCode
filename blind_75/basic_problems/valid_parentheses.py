class Solution:
    def isValid(self, s: str) -> bool:
        #define a dictionary with valid pairs
        pair ={
            ")":"(",
            "]":"[",
            "}":"{"
        }

        #define a stack
        stack =[]
        #using a for loop iterate over the strings
        for char in s:
            #using a if statement check if the char is valid opening paranthese
            if char in "({[":
                #append only if its a opening bracket
                stack.append(char)
            else:
                #if the stack doesn't have the valid  opening bracket
                if not stack:
                    return False

            #now check if the last entered element in the stack has a matching pair in pair
                if stack[-1] != pair[char]:
                    return False
            #if it has a valid pair then pop the element from stack.
            
                stack.pop()
        return len(stack) == 0
    


        

            