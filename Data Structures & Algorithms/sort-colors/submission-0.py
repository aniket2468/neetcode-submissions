class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zeros = 0
        ones = 1
        for i in range(n):
            if nums[i] == 0:
                zeros += 1
            elif nums[i] == 1:
                ones += 1
        
        for i in range(0, zeros):
            nums[i] = 0
        for i in range(zeros, zeros + ones - 1):
            nums[i] = 1
        for i in range(zeros + ones - 1, n):
            nums[i] = 2

