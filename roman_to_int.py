class Solution:
    def __init__(self):
         self.roman_to_int_map = {
            'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000
        }

    def romanToInt(self, s: str) -> int:
          result = 0
          previous_value = 0
          for char in reversed(s):
            current_value = self.roman_to_int_map[char]
            if current_value < previous_value:
                result -= current_value
            else:
                result += current_value
            previous_value = current_value
          return result
converter = Solution()
print(converter.romanToInt("XII"))

    
