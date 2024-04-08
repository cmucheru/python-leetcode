class Solution:
    def isPalindrome(self, number):
        num_str = str(number)
        reversed = num_str[::-1]
        if num_str == reversed:
            return True
        else:
            return False
