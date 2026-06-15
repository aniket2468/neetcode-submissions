class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)
        for key in s:
            s_dict[key] += 1
        for key in t:
            s_dict[key] -= 1
            if s_dict[key] == 0:
                del s_dict[key]
        
        return len(s_dict) == 0