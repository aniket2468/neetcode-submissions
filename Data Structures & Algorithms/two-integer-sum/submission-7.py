class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_dict = defaultdict(int)
        for i in range(len(nums)):
            map_dict[nums[i]] = i
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in map_dict and map_dict[complement] != i:
                return [i, map_dict[complement]]

        return [-1, -1]