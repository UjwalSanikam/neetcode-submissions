class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        for i in range(len(temperatures)):
            if temperatures[i] == max(temperatures[i:]):
                stack.append(0)
            else:
                j = i + 1
                while j < len(temperatures) and temperatures[j] <= temperatures[i]:
                    j = j + 1
                stack.append(j-i)
        return stack 
