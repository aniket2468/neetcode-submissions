class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}

        for i in nums:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
        
        values = []

        for i in m:
            values.append((i, m[i]))
        
        values.sort(key = lambda x: x[-1], reverse = True)

        ans = []

        for i, j in values:
            ans.append(i)
        return ans[:k]