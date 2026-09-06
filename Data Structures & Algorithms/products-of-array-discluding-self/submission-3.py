class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, sufix, res = [1] * n, [1] * n, [0] * n

        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        for i in range(n-2, -1, -1):
            sufix[i] = sufix[i+1] * nums[i+1]
        
        for i in range(n):
            res[i] = prefix[i] * sufix[i]
        
        return res