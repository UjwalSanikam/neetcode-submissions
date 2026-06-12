class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict1 = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                elif dict1[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
        

