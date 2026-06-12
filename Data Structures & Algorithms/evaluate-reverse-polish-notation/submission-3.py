class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b
            }
        for i in range(len(tokens)):
            if(tokens[i] in ['+', '-', '*', '/']):
                b = int(stack.pop())
                a = int(stack.pop())
                result = ops[tokens[i]](a, b)
                stack.append(result)
            else:
                stack.append(tokens[i])
        return int(stack.pop())