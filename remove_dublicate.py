class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = list(dict.fromkeys(nums))
        for i in range(len(unique)):
          nums[i] = unique[i]
        return len(unique)
