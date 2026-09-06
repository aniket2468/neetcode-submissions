class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_dict = defaultdict(int)
        for i, num in enumerate(nums):
            map_dict[num] = i
        
        for num, i in enumerate(nums):
            complement = target - i
            if complement in map_dict and map_dict[complement] != num:
                return [num, map_dict[complement]]
        return [0, 0]