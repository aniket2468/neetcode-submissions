class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
    
        # Dictionary to store the count of characters in t
        t_count = Counter(t)
        current_count = {}
        
        # Two pointers and variables to track the window
        left = 0
        right = 0
        required = len(t_count)
        formed = 0
        min_len = float('inf')
        min_window = (None, None)
        
        # Start sliding the window
        while right < len(s):
            char = s[right]
            current_count[char] = current_count.get(char, 0) + 1
            
            # Check if the current character satisfies the condition in t
            if char in t_count and current_count[char] == t_count[char]:
                formed += 1
            
            # Try to contract the window
            while left <= right and formed == required:
                char = s[left]
                
                # Update minimum window
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window = (left, right)
                
                # Remove the leftmost character from the window
                current_count[char] -= 1
                if char in t_count and current_count[char] < t_count[char]:
                    formed -= 1
                
                left += 1
            
            # Expand the window
            right += 1
        
        # Extract the substring
        start, end = min_window
        return "" if min_window[0] is None else s[start:end + 1]