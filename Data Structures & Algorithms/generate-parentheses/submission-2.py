class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(openN, closedN, curr):
            if openN ==closedN == n:
                res.append(curr)
                return
            if openN < n:
                backtrack(openN + 1, closedN, curr + '(')
            if closedN < openN:
                backtrack(openN, closedN + 1, curr + ')')
        
        backtrack(0, 0, '')
        return res