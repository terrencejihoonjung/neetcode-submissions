class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1: return int(tokens[0])

        stack = []
        for token in tokens:
            self.perform_operation(stack, token)
        
        return stack[0]
    
    def perform_operation(self, stack, token) -> None:

        match(token):
            case "+":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                stack.append(num1 + num2)
            case "-":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                stack.append(num2 - num1)
            case "*": 
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                stack.append(num1 * num2)
            case "/":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                stack.append(int(num2 / num1))
            case _:
                stack.append(token)
