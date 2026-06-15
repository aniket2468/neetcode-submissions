class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        import bisect
        for num in nums:
            idx = bisect.bisect_left(tails, num)

            if idx == len(tails):
                tails.append(num)
            else:
                tails[idx] = num
        return len(tails)