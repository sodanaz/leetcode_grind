class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0
        while l<=r:
            mid = l + (r-l)//2
            if mid ** 2 == x:
                return mid
            elif mid**2 > x:
                r = mid - 1
            else:
                res = mid
                l = mid + 1
        return res