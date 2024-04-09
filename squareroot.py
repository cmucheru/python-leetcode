import math
class Solution:
    def mySqrt(self, x: int) -> int:
        x_sq = int(math.sqrt(x))
        x_fl = math.floor(x_sq)
        return x_fl
