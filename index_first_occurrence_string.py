class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:  # Handle empty needle case
            return 0
        
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        
        return -1  # Return -1 if needle is not found in haystack
