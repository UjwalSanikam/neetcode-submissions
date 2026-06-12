class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        stack = []
        for char in s:
            if char in stack:
                stack = stack[stack.index(char)+1:]
            stack.append(char)
            if len(stack) > longest:
                longest = len(stack)
        return longest

                    