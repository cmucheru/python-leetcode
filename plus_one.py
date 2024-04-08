class Solution:
    def plusOne(self, digits):
        nums = 0
        for digit in digits:
            nums = nums * 10 + digit
        nums += 1
        result = []
        for my_num in str(nums):
            result.append(int(my_num))
        return result
