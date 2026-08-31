class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {")": "(", "]": "[", "}": "{"}
        stack = [] # stores all the opening brackets seen

        for char in s:
            if char in hashMap.values(): # add to stack if opening bracket
                stack.append(char)
            else: 
                if not stack:
                    return False

                if stack[-1] != hashMap[char]: # checks recent opening bracket with current closing bracket
                    return False
                
                stack.pop()     # have a matching bracket pair

        return len(stack) == 0
