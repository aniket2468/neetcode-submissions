class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        visited_num = set()
        for i in range(len(nums)):
            if nums[i] in visited_num:
                return nums[i]
            visited_num.add(nums[i])