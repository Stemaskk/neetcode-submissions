class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []

        def backtrack(openP, closeP, stack):
            if openP == closeP == n:
                result.append("".join(stack))
                return

            if openP < n:
                stack.append("(")
                backtrack(openP + 1, closeP, stack)
                stack.pop()
            
            if closeP < openP:
                stack.append(")")
                backtrack(openP, closeP + 1, stack)
                stack.pop()

        backtrack(0, 0, [])

        return result