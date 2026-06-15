class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def rec_bracket(openedN, closedN):
            if openedN == closedN == n:
                res.append("".join(stack))
                return
            
            if openedN < n:
                stack.append("(")
                rec_bracket(openedN + 1, closedN)
                stack.pop()
            
            if closedN < openedN:
                stack.append(")")
                rec_bracket(openedN, closedN + 1)
                stack.pop()
        
        rec_bracket(0, 0)
        return res