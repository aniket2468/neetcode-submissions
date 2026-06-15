class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for key in s:
            s_dict[key] = s_dict.get(key, 0) + 1
        for key in t:
            t_dict[key] = t_dict.get(key, 0) + 1
        
        return s_dict == t_dict