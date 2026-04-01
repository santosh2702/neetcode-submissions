class Solution:
    def isPalindrome(self, s: str) -> bool:
        Str = ''
        for c in s:
            if c.isalnum():
                Str += c.lower()
        return Str == Str[::-1]