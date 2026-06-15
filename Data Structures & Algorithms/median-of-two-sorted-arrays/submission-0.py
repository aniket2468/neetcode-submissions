class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        if len(nums3) & 1:
            return nums3[len(nums3) // 2]
        return (nums3[len(nums3) // 2] + nums3[(len(nums3) - 1) // 2])/2