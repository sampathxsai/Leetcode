import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        x = math.log2(n)

        if x % 1 == 0:
            return True
        else:
            return False