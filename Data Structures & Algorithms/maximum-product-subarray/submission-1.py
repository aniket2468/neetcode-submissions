class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = minProd = ans = nums[0]

        for num in nums[1:]:
            if num < 0:
                minProd, maxProd = maxProd, minProd
            minProd = min(num, minProd * num)
            maxProd = max(num, maxProd * num)
            ans = max(maxProd, ans)
        return ans