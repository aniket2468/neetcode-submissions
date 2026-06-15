class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtracking(start, path):
            res.append(path.copy())
            for i in range(start, len(nums)):
                if i > start and nums[i-1] == nums[i]:
                    continue
                path.append(nums[i])
                backtracking(i+1, path)
                path.pop()
        backtracking(0, [])
        return res
