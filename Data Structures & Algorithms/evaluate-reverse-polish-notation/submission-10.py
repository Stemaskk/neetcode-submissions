class Solution:
    def evalRPN(self, tokens: List[str]) -> int:        
        result = []

        for i in range(len(tokens)):
            match tokens[i]:
                case "+":
                    a = result[-1]
                    result.pop()
                    b = result[-1]
                    result.pop()
                    result.append(a + b)
                case "-":
                    a = result[-1]
                    result.pop()
                    b = result[-1]
                    result.pop()
                    result.append(b - a)
                case "*":
                    a = result[-1]
                    result.pop()
                    b = result[-1]
                    result.pop()
                    result.append(a * b)
                case "/":
                    a = result[-1]
                    result.pop()
                    b = result[-1]
                    result.pop()
                    result.append(int(b / a))
                case _:
                    result.append(int(tokens[i]))

        return result[0]
