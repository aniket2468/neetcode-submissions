class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_dict = defaultdict(int)
        for i in s:
            map_dict[i] += 1
        for i in t:
            map_dict[i] -= 1
            if map_dict[i] == 0:
                del map_dict[i]
        
        return len(map_dict) == 0