class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapdict = {}
        for i, num in enumerate(nums):
            mapdict[num] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in mapdict and mapdict[complement] != i:
                return [i, mapdict[complement]]
        
        return [-1,-1]