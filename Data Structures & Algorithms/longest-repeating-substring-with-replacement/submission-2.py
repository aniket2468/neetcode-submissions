class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        h_map = {}
        res = 0
        left = 0
        max_freq = 0
        for right in range(len(s)):
            h_map[s[right]] = h_map.get(s[right], 0) + 1
            max_freq = max(max_freq, h_map[s[right]])
            while (right - left + 1) - max_freq > k:
                h_map[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res