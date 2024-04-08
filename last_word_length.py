class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        text = s.strip()
        words = text.split()
        if words:
            return len(words[-1])
        else:
            return None
# Example usage
text = "      hello     world                "
solution = Solution()
last_word = solution.lengthOfLastWord(text)
print(last_word)  # Output: world
        
