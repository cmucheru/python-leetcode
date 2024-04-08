from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the seen numbers along with their indices
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            # Check if the complement is already in the dictionary
            if complement in seen:
                # If found, return the indices of the two numbers
                return [seen[complement], i]

            # If not found, add the current number to the dictionary
            seen[num] = i

        # If no solution is found
        return []
