class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'(':')', '[':']', '{':'}'}
        count  = 1
        stack = []
        for p in s:
            if p in mapping:
                stack.append(p)
            elif len(stack) == 0 or p != mapping[stack.pop()]:
                return False
        return len(stack) == 0
