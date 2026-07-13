class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left = 1
        right = x
        while right - left > 1:
            mid = (left + right) // 2
            if mid ** 2 <= x:
                left = mid
            elif mid ** 2 > x:
                right = mid
        return left

        