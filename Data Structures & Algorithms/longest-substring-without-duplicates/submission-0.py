class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                first_char = s[i : j+1]
                if len(set(first_char)) == len(first_char):
                    if len(first_char) > count:
                        count = len(first_char)
                else:
                    break 
        return count