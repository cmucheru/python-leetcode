class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
       my_list = []
       for digit in range(1,n+1): 
              if digit % 3==0 and digit% 5==0:
                    my_list.append("FizzBuzz")
              elif digit % 3==0 :
                    my_list.append("Fizz")
              elif digit% 5==0:
                     my_list.append("Buzz")
              else:
                    my_list.append(str(digit))
       return my_list
print(Solution().fizzBuzz(3))
            
