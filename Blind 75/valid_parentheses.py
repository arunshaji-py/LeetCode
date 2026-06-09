class Solution:
    def isValid(self, s: str) -> bool:
        pair = {
            ")":"(", 
            "]":"[",
            "}":"{"
        }

        stack = []
        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack:
                    return False
                
            
                if stack[-1] != pair[char]:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0
        

             