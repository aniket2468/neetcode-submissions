class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        stored_nums = {}
        
        for i in range(len(nums)):
            stored_nums[nums[i]] = i
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in stored_nums and stored_nums[complement] != i:
                return [i, stored_nums[complement]]
        return []