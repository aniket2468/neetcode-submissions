class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_simplified = re.sub(r'[^0-9a-zA-Z]', '', s).lower()
        return s_simplified == s_simplified[::-1]