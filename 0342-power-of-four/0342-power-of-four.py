class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n >= 1:
            if n == 1:
                return True
            else:
                n = n/4
        return False